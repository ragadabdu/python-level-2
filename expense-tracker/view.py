import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from data import load_data, save_data


expenses, category_menu = load_data()

def view_list(sorted_list):
    for i, expense in enumerate(sorted_list, start = 1):
        date_obj = datetime.fromisoformat(expense["date"])
        print(f'{i}. item: {sorted_list[i-1]["item"]} - category: {sorted_list[i-1]["category"]} - amount: {sorted_list[i-1]["amount"]} - date: {date_obj.strftime("%Y-%m-%d")}')

def add_expense(expenses,category_menu):
    print(category_menu)
    category = input("choose a category: ").lower().strip()
    if category in category_menu:
        expenses.append({"item": input("enter item: "), "category": category, "amount": int(input("enter amount: ")), "date": datetime.now().isoformat()})
        save_data()
    else:
        print("This category doesn't exist. You can create it by choosing 'editing category'.")

def plot_graph(expenses):
    category_totals = defaultdict(int)
    for expense in expenses:
        category_totals[expense["category"]] += expense["amount"]
        
    category = list(category_totals.keys())
    amount = list(category_totals.values())

    plt.pie(amount, labels = category, autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.show()

def delete_expense(expenses):
    index = input("enter index of expense to delete: ")
    if not index.isdigit():
        print("Invalid input. Enter a number.")
    elif int(index)-1 <= 0:
        print("Invaild number. Index cannot be a zero or a negative number.")
    elif int(index) >= len(expenses):
        print("Invaild number. No expense is associated with this number.")
    else:
        expenses.pop(int(index)-1)

def view_expenses(expenses,category_menu):
    view_options = input("Do you want to: Sort?Filter?View?: ").lower()
    if view_options == "view":
        view_list(expenses)
    elif view_options == "sort":
        sort_option = input("Sort by: Category?Item?Amount?: ").lower()
        if sort_option == "category":
            order = input("From: A-Z? Z-A?: ").lower()
            reversed = (order == "z-a")
            sorted_list = sorted(expenses, key = lambda x: x["category"], reverse=reversed)
            view_list(sorted_list)

        elif sort_option == "item":
            order = input("From: A-Z? Z-A?: ").lower()
            reversed = (order == "z-a")
            sorted_list = sorted(expenses, key = lambda x: x["item"], reverse=reversed)
            view_list(sorted_list)

        elif sort_option == "amount":
            order = input("Order: Ascending? Descending?: ").lower()
            reversed = (order == "descending")
            sorted_list = sorted(expenses, key = lambda x: x["item"], reverse=reversed)
            view_list(sorted_list)
        elif view_options == "filter":
            filter_option = input("Filter by: Category? Item? Amount? ").lower()
            if filter_option == "category":
                filter_by = input(f"pick category to filter: {category_menu}? ")
                filtered_list = [expense for expense in expenses if expense["category"] == filter_by]
                view_list(filtered_list)
            elif filter_option == "item":
                filter_by = input("Filter by item name: ")
                filtered_list = [expense for expense in expenses if expense["item"] == filter_by]
                view_list(filtered_list)
            if filter_option == "amount":
                min_amount = int(input("Enter minimum amount: "))
                max_amount = int(input("Enter maximum amount: "))
                filtered_list = [expense for expense in expenses if min_amount <= expense["amount"] <= max_amount]
                view_list(filtered_list)

def edit_category(expenses,category_menu):
    while True:
        editing_option = input("choose action:Add?Delete?Summary?back? ").lower().strip()

        if editing_option == "back":
            break

        elif editing_option == "add":
            new_category = input("enter new category: ")
            if new_category in category_menu:
                print("Category already exists.")
            else:
                category_menu.append(new_category)
                print(category_menu)
                print("New category added successfully!")
        elif editing_option == "delete":
            for n, category in enumerate(category_menu, start = 1):
                print(category)
                index = input("Enter index number for the category: ")
                if index.isdigit() and int(index) <= len(category_menu) and int(index) > 0:
                    category_to_delete = category_menu[int(index)-1]
                    if any(expense["category"] == category_to_delete for expense in expenses):
                        confirm = input("You have expenses in this category are you sure you want to delete(y/n):").lower()
                        if confirm == "y":
                            category_menu.pop(int(index)-1)
                    else:
                        category_menu.pop(int(index)-1)
        elif editing_option == "summary":
            for category in category_menu:
                total_amount = 0
                for expense in expenses:
                    if category == expense["category"]:
                        total_amount += expense["amount"]
                print(f'Total amount: {total_amount} in {category}')

def edit_expenses(expenses,category_menu):
    while True:
        index = input("Enter index of expense: ")

        if index == "back":
            break

        elif index.isdigit() and int(index) <= len(expenses) and int(index) > 0:
            editing_expense = input("do you want to edit: category?item?amount?back?").lower().strip()
            if editing_expense =="back":
                break
            elif editing_expense == "category":
                diff_category = input("enter a different category: ")
                if diff_category in category_menu:
                    expenses[int(index)-1]["category"] = diff_category
                else:
                    print("This category doesn't exist. You can create it by choosing 'editing category'.")
            elif editing_expense == "item":
                expenses[int(index)-1]["item"]=input("enter a different item: ")

            elif editing_expense == "amount":
                diff_amount = input("enter a different amount:")
                if diff_amount.isdigit():
                    expenses[int(index)-1]["amount"] = int(diff_amount)
                else:
                    print("Invalid amount")
        else:
            print("Invalid index number.")