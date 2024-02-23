import json
import argparse
import os
from os.path import exists, dirname


def parse_arguements():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-m", "--message", type=str, nargs="*")
    parser.add_argument("-l","--model", type=str, default="mistral", choices=["mistral", "llama2", "gemma", "gemma:2b", "gemma:7b "])
    
    args = parser.parse_args()
    
    return args.message, args.model

def parse_answer_to_json(answer: str, ground_truth: str, idx: int) -> dict:
    
    dict_ = {
        "index": idx,
        "result": answer,
        "ground_truth": ground_truth
        }

    return dict_

def save_json(model: str, dict_: dict):
    name = f"./output/{model}_test/review_{dict_['index']}.json"
    
    create_folder("./output", False)
    create_folder(name, True)
    with open(name, "w") as outfile:
        json.dump(dict_, outfile)
        
def create_folder(path:str, dirname_: bool=False):   
    
    if dirname_:
        if not exists(dirname(path)):
            os.mkdir(dirname(path))
    else:
        if not exists(path):
            os.mkdir(path)
    