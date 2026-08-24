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
    print("4: exit")

def list():
    file = Path("dict.json")
    with open(file, "r") as todo
    data = json.load(todo)
    print(data)
def add():

def remove():

while True:
    menu()
    choice = input("enter your choice: ")

    if choice == 1:
        list()
    elif choice == 2:
        print("we don't have that rn my nigga")
    elif choice == 3:
        print("we don't have that rn bluddy")
    elif choice == 4:
        break
    else:
        print(f"invalid choice: {choice}")
