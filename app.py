from pathlib import Path
import json
import keyboard
import os

class TodoApp:
    def __init__(self):
        file = Path("dict.json")

        if not file.exists() or file.stat().st_size == 0:
            self.write = {"tasks": []}
            with open(file, "w") as f:
                json.dump(self.write, f)

    def menu(self):
        print("1: list")
        print("2: add")
        print("3: remove")
        print("4: exit")

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def list(self):
        self.clear()
        file = Path("dict.json")
        with open(file, "r") as f:
            self.data = json.load(f)

        for task in self.data["tasks"]:
            print(f"[{task['id']}] {task['title']}")

    def add(self):
        file = Path("dict.json")
        self.list()
        useri = input("\nwhat do you want to add?: ")
        with open(file, "r") as f:
            self.data = json.load(f)
            add_todo = {"id": len(self.data["tasks"]) + 1, "title": useri}
            self.data["tasks"].append(add_todo)

            with open(file, "w") as f:
                if useri == "":
                    return
                else:
                    json.dump(self.data, f)

    def remove(self):
        file = Path("dict.json")
        with open(file, "r") as f:
            self.data = json.load(f)
        self.list()
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
        app.clear()
        app.menu()
        choice = input("enter your choice: ")
        if choice == "1":
            app.list()
            input("\npress enter to continue..")
        elif choice == "2":
            app.add()
        elif choice == "3":
            app.remove()
        elif choice == "4":
            app.clear()
            break
        else:
            print(f"invalid choice: {choice}")
