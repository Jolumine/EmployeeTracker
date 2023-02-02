import json 
import os

def prepare() -> None: 
    if os.path.exists("index.json"):
        pass 
    else: 
        with open("index.json", "w") as f: 
            json.dump({}, f, indent=4, sort_keys=False)
            f.close()


