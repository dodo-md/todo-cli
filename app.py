from pathlib import Path
import json

class TodoApp:
    def __init__(self):
        file = Path("dict.json")
        if not file.exists():
            self.write = {"tasks": []}
            with open(file, "w") as f:
                data = json.dump(self.write, f)

    def menu(self):
        print("1: list")
        print("2: add")
        print("3: remove")
        print("4: exit")

    def list(self):
        file = Path("dict.json")
        with open(file, "r") as f:
            self.data = json.load(f)
            print(self.data)

    def add(self):
        file = Path("dict.json")
        useri = input("what do you want to add?: ")
        with open(file, "r") as f:
            self.data = json.load(f)
            add_todo = {"id": len(self.data["tasks"]) + 1, "title": useri}
            self.data["tasks"].append(add_todo)

            with open(file, "w") as f:
                json.dump(self.data, f)

    def remove(self):
        file = Path("dict.json")
        with open(file, "r") as f:
            self.data = json.load(f)
        print(self.data)
        useri = input("which task do you want to delete?: ")

        try:
            useri = int(useri)
        except ValueError:
            print(f"wrong format: {useri}")
            return

        for i, task in enumerate(self.data["tasks"]):
            if task["id"] == useri:
                self.data["tasks"].pop(i)
                break
        else:
            print(f"wrong id: {useri}")

        with open(file, "w") as f:
            json.dump(self.data, f)

if __name__ == "__main__":
    app = TodoApp()

    while True:
        app.menu()
        choice = input("enter your choice: ")
        if choice == "1":
            app.list()
        elif choice == "2":
            app.add()
        elif choice == "3":
            app.remove()
        elif choice == "4":
            break
        else:
            print(f"invalid choice: {choice}")
