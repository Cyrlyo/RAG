import requests
import subprocess
import ollama


class llm():
    def __init__(self) -> None:
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

    def connect(self):
        client = ollama.Client(host='http://localhost:11434')
        return client