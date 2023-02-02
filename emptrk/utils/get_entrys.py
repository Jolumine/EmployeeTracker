import json

def get_entrys(filter=""):
    collection = []
    with open("index.json", "r") as f: 
        parsed = json.load(f)
        f.close()

    if filter != "":
        for entry in parsed: 
            if filter in parsed[entry]["Firstname"] or filter in parsed[entry]["Lastname"] or filter in parsed[entry]["Position / Description"]:
                collection.append(f'{entry}-{parsed[entry]["Firstname"]}-{parsed[entry]["Lastname"]}')
            else: 
                continue
    else: 
        for entry in parsed: 
            collection.append(f'{entry}-{parsed[entry]["Firstname"]}-{parsed[entry]["Lastname"]}')

    return collection
