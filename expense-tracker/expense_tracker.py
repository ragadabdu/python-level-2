#
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

try:
    with open("data.json", "r") as f:
        data = json.load(f)
        expenses = data.get("expenses", [])
        category_menu = data.get("category_menu", ["bills", "food", "school"])
except FileNotFoundError:
    expenses = []
    category_menu = ["bills", "food", "school"]

def save_data():
    with open("data.json", "w") as f:
        json.dump({"expenses": expenses ,"category_menu": category_menu}, f)

while True:
    action = input("Choose option:Add?View?Delete?Edit Expense?Edit Category?Show graph?Exit? ").lower().strip()

    if action == "exit":
        break

    elif action == "add":
        print(category_menu)
        category = input("choose a category: ").lower().strip()
        if category in category_menu:
            expenses.append({"item": input("enter item: "), "category": category, "amount": int(input("enter amount: ")), "date": datetime.now().isoformat()})
            save_data()
        else:
            print("This category doesn't exist. You can create it by choosing 'editing category'.")
    
    elif action == "view":
        view_options = input("Do you want to: Sort?Filter?View?: ").lower()
        if view_options == "view":
            for i, expense in enumerate(expenses, start = 1):
                date_obj = datetime.fromisoformat(expense["date"])
                print(f'{i}. item: {expenses[i-1]["item"]} - category: {expenses[i-1]["category"]} - amount: {expenses[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
        elif view_options == "sort":
            sort_option = input("Sort by: Category?Item?Amount?: ").lower()
            if sort_option == "category":
                order = input("From: A-Z? Z-A?: ").lower()
                if order == "a-z":
                    sorted_list = sorted(expenses, key = lambda x: x["category"])
                    for i, expense in enumerate(sorted_list, start = 1):
                        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
                else: 
                    sorted_list = sorted(expenses, key = lambda x: x["category"], reverse= True)
                    for i, expense in enumerate(sorted_list, start = 1):
                        date_obj = datetime.fromisoformat(expense["date"])
                        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')

            elif sort_option == "item":
                order = input("From: A-Z? Z-A?: ").lower()
                if order == "a-z":
                    sorted_list = sorted(expenses, key = lambda x: x["item"])
                    for i, expense in enumerate(sorted_list, start = 1):
                        date_obj = datetime.fromisoformat(expense["date"])
                        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
                else: 
                    sorted_list = sorted(expenses, key = lambda x: x["item"], reverse=True)
                    for i, expense in enumerate(sorted_list, start = 1):
                        date_obj = datetime.fromisoformat(expense["date"])
                        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')

            elif sort_option == "amount":
                order = input("Order: Ascending? Descending?: ").lower()
                if order == "ascending":
                    sorted_list = sorted(expenses, key = lambda x: x["amount"])
                    for i, expense in enumerate(sorted_list, start = 1):
                        date_obj = datetime.fromisoformat(expense["date"])
                        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
                else: 
                    sorted_list = sorted(expenses, key = lambda x: x["amount"], reverse=True)
                    for i, expense in enumerate(sorted_list, start = 1):
                        date_obj = datetime.fromisoformat(expense["date"])
                        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
        elif view_options == "filter":
            filter_option = input("Filter by: Category? Item? Amount? ").lower()
            if filter_option == "category":
                filter_by = input(f"pick category to filter: {category_menu}? ")
                filtered_list = [expense for expense in expenses if expense["category"] == filter_by]
                for i, expense in enumerate(filtered_list, start = 1):
                    date_obj = datetime.fromisoformat(expense["date"])
                    print(f'{i}. item: {filtered_list[i-1]["item"]} - category: {filtered_list[i-1]["category"]} - amount: {filtered_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
            elif filter_option == "item":
                filter_by = input("Filter by item name: ")
                filtered_list = [expense for expense in expenses if expense["item"] == filter_by]
                for i, expense in enumerate(filtered_list, start = 1):
                    date_obj = datetime.fromisoformat(expense["date"])
                    print(f'{i}. item: {filtered_list[i-1]["item"]} - category: {filtered_list[i-1]["category"]} - amount: {filtered_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
            if filter_option == "amount":
                min_amount = int(input("Enter minimum amount: "))
                max_amount = int(input("Enter maximum amount: "))
                filtered_list = [expense for expense in expenses if min_amount <= expense["amount"] <= max_amount]
                for i, expense in enumerate(filtered_list, start = 1):
                    date_obj = datetime.fromisoformat(expense["date"])
                    print(f'{i}. item: {filtered_list[i-1]["item"]} - category: {filtered_list[i-1]["category"]} - amount: {filtered_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')
    elif action == "edit expense":
        index = input("Enter index of expense: ")
        if index =="back":
                continue
        if index.isdigit() and int(index) <= len(expenses) and int(index) > 0:
            editing_expense = input("do you want to edit: category?item?amount?back?").lower().strip()
            if editing_expense =="back":
                continue
            if editing_expense == "category":
                diff_category = input("enter a different category: ")
                if diff_category in category_menu:
                    expenses[int(index)-1]["category"] = diff_category
                    save_data()
                else:
                    print("This category doesn't exist. You can create it by choosing 'editing category'.")
            elif editing_expense == "item":
                expenses[int(index)-1]["item"]=input("enter a different item: ")
                save_data()
            elif editing_expense == "amount":
                diff_amount = input("enter a different amount:")
                if diff_amount.isdigit():
                    expenses[int(index)-1]["amount"] = int(diff_amount)
                    save_data()
                else:
                    print("Invalid amount")
        else:
            print("Invalid index number.")

    elif action == "edit category":
        editing_option = input("choose action:Add?Delete?Summary?back? ").lower().strip()

        if editing_option =="back":
            continue
        if editing_option == "add":
            new_category = input("enter new category: ")
            if new_category in category_menu:
                print("Category already exists.")
            else:
                category_menu.append(new_category)
                save_data()
        elif editing_option == "delete":
            for n, cate in enumerate(category_menu, start = 1):
                print(cate)
            index = input("Enter index number for the category: ")
            if index.isdigit() and int(index) <= len(category_menu) and int(index) > 0:
                category_to_delete = category_menu[int(index)-1]
                if any(expense["category"] == category_to_delete for expense in expenses):
                    confirm = input("You have expenses in this category are you sure you want to delete(y/n):").lower()
                    if confirm == "y":
                        category_menu.pop(int(index)-1)
                else:
                    category_menu.pop(int(index)-1)
            save_data()
        elif editing_option == "summary":
            for cate in category_menu:
                total_amount = 0
                for expense in expenses:
                    if cate == expense["category"]:
                        total_amount += expense["amount"]
                print(f'Total amount: {total_amount} in {cate}')


    elif action == "show graph":
        category_totals = defaultdict(int)
        for expense in expenses:
            category_totals[expense["category"]] += expense["amount"]
        
        labels = list(category_totals.keys())
        y = list(category_totals.values())

        plt.pie(y, labels = labels)
        print(category_totals)

        plt.title("Expenses by Category")
        plt.show()

    elif action == "delete":
        index = input("enter index of expense to delete: ")
        if not index.isdigit():
            print("Invalid input. Enter a number.")
        elif int(index)-1 <= 0:
            print("Invaild number. Index cannot be a zero or a negative number.")
        elif int(index) >= len(expenses):
            print("Invaild number. No expense is associated with this number.")
        else:
            expenses.pop(int(index)-1)
            save_data()




        