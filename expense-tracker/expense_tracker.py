#

expenses = []

category_menu = ["bills", "food", "school"]

while True:
    action = input("Choose option:Add?View?Delete?Edit Expense?Edit Category?Exit? ").lower().strip()

    if action == "exit":
        break

    elif action == "add":
        print(category_menu)
        category = input("choose a category: ").lower().strip()
        if category in category_menu:
            expenses.append({"item": input("enter item: "), "category": category, "amount": input("enter amount: ")})
        else:
            print("This category doesn't exist. You can create it by choosing 'editing category'.")
    
    elif action == "view":
        for i, expense in enumerate(expenses, start = 1):
            print(f'{i}. item: {expenses[i-1]["item"]} - category: {expenses[i-1]["category"]} - amount: {expenses[i-1]["amount"]}')
    
    elif action == "edit expense":
        index = input("Enter index of expense: ")
        editing_expense = input("do you want to edit: category?item?amount?exit?").lower().strip()
        if editing_expense =="exit":
            continue
        if index.isdigit() and int(index) <= len(expenses):
            if editing_expense == "category":
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
                    expenses[int(index)-1]["amount"] = diff_amount
                else:
                    print("Invalid amount")
        else:
            print("Invalid index number.")

    elif action == "edit category":
        editing_option = input("choose action:Add?Delete?Summary? ").lower().strip()

        if editing_option =="exit":
            continue
        if editing_option == "add":
            new_category = input("enter new category: ")
            if new_category in category_menu:
                print("Category already exists.")
            else:
                category_menu.append(new_category)
        elif editing_option == "summary":
            for cate in category_menu:
                total_amount = 0
                for expense in expenses:
                    if cate == expense["category"]:
                        total_amount += int(expense["amount"])
                print(f'Total amount: {total_amount} in {cate}')

    elif action == "delete":
        index = input("enter index of expense to delete: ")
        if index.isdigit() and int(index) <= len(expenses):
            expenses.pop(int(index)-1)



        