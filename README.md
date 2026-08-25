# todo-cli

A minimal command-line to-do list manager written in Python. Tasks are stored locally in a JSON file, so your list persists between runs.

## Features

- List all tasks
- Add a new task
- Remove a task by ID
- JSON-based storage (`dict.json`), created automatically on first run

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/todo-cli.git
cd todo-cli
uv sync
```

## Usage

Run the app:

```bash
uv run app.py
```

You'll see a simple menu:

```
1: list
2: add
3: remove
4: exit
```

Enter the number of the action you want to perform and follow the prompts.

## Project Structure

```
todo-cli/
├── app.py          # Main application logic (TodoApp class)
├── dict.json        # Local task storage (auto-generated)
└── pyproject.toml   # Project metadata
```
