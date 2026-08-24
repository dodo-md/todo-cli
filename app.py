from pathlib import Path
import json

data = []

def __init__():
    file = Path("dict.json")
    if not file.exists():
        with open(file, "w") as jsof:
            json.dump(data, jsof)

def menu():
    print("1: list")
    print("2: add")
    print("3: remove")

__init__()
