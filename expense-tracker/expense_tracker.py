#

expenses = []

category_menu = ["bills", "food", "school"]

while True:
    action = input("Choose option:Add?View?Delete?Edit Category?Exit? ").lower().strip()

    if action == "exit":
        break

    elif action == "add":
        print(category_menu)
        category = input("choose a category: ").lower().strip()
        expenses.append({"item": input("enter item: "), "category": category, "amount": int(input("enter amount: "))})
    
    elif action == "view":
        for i, expense in enumerate(expenses, start = 1):
            print(f'{i}. item: {expenses[i-1]["item"]} - category: {expenses[i-1]["category"]} - amount: {expenses[i-1]["amount"]}')

    elif action == "edit category":
        editing_option = input("choose action:Add?Delete?Summary? ").lower().strip()

        if editing_option =="exit":
            break
        elif editing_option == "add":
            category_menu.append(input("enter new category: "))
        elif editing_option == "summary":
            for cate in category_menu:
                total_amount = 0
                for expense in expenses:
                    if cate == expense["category"]:
                        total_amount += expense["amount"] 
                print(total_amount)
                print(cate)

    elif action == "delete":
        index = int(input("enter index of expense to delete: "))
        expenses.pop(index-1)


        