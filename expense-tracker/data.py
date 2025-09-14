import json
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            expenses = data.get("expenses", [])
            category_menu = data.get("category_menu", ["bills", "food", "school"])
    except FileNotFoundError:
        expenses = []
        category_menu = ["bills", "food", "school"]
    return expenses, category_menu

def save_data(expenses, category_menu):
    with open(DATA_FILE, "w") as f:
        json.dump({"expenses": expenses ,"category_menu": category_menu}, f)