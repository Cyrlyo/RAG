import ollama
import requests
import subprocess
import time
import pandas as pd
from tqdm import tqdm
from utils import parse_arguements, parse_answer_to_json, save_json
import prompt

#TODO: refactor
#TODO: Add log
#TODO: create a Git's repo
#TODO: llama2 result different that Mistral need to change the output 

# Check if Ollama is running, if not it'll open a new shell on launch it.
try:
    url_response = requests.get('http://localhost:11434')
    print("Ollama already launched.\n")
except:
    subprocess.run(["powershell", "Start-Process", "powershell", "-ArgumentList", f"'-NoExit', '-Command', 'ollama serve'"])    
    stop = True
    while stop:
        try:
            url_response = requests.get('http://localhost:11434')
            print("Ollama has been launched.\n")
            stop = False
        except:
            None
            

ollama = ollama.Client(host='http://localhost:11434')



def ask_mistral_sentiment(model: str, review: str) -> str:
    
    # response = ollama.chat(model=model, messages=[{

    #     "role": "user",
    #     "content": f"Give me the sentiment of this review: {review}. Answer with 1 word, 'positive' or 'negative'",

    # },])
    
    zeroshot = prompt.zeroshot()
    
    response = ollama.chat(model=model, messages=[zeroshot.sentiment_basics(review)])
    
    if model == "mistral":
        answer = response["message"]["content"][1:].replace(".", "").lower()
    
    else:
        answer = response["message"]["content"].replace(".", "").lower()
    print(answer)
    
    if len(response["message"]["content"][1:].split(" ")) > 1:
        answer = answer.split(" ")[0]
        print(answer)

    return answer

def ask_mistral(model: str, message: str) -> str:
    
    response = ollama.chat(model=model, messages=[{

        "role": "user",
        "content": message,

    },])

    return response["message"]["content"][1:]

if __name__ == "__main__":

    message, model = parse_arguements()

    print(f"{model} has been loaded")
    
    
    data = pd.read_csv("./data/IMDB_Dataset.csv")
    
    print(ask_mistral(model, message[0]))
    
    # if len(message) > 1:
        # for msg in message:
            # print(f"{msg}\n")
            # ask_mistral_sentiment(model, msg)
    # else:
        # print(f"'{message[0]}'")
        # ask_mistral_sentiment(model, message[0])


    # for idx in tqdm(data.index):
    
    for idx in data.index:
        
        if idx < 2484:
            review = data["review"][idx]
            print(f"----\n{data["sentiment"][idx]}")
            answer = ask_mistral_sentiment(model, review)
            answer_parsed = parse_answer_to_json(answer, data["sentiment"][idx], idx)
            save_json(model, answer_parsed)
    