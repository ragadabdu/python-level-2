from view import add_expense,view_expenses,edit_category,edit_expenses,delete_expense,plot_graph
from data import load_data, save_data

expenses, category_menu = load_data()

while True:
    action = input("Choose option:Add?View?Delete?Edit Expense?Edit Category?Show graph?Exit? ").lower().strip()

    if action == "exit":
        break

    elif action == "add":
        add_expense(expenses, category_menu )
        save_data(expenses, category_menu)
    
    elif action == "view":
        view_expenses(expenses, category_menu )

    elif action == "edit expense":
        edit_expenses(expenses, category_menu )
        save_data(expenses, category_menu)

    elif action == "edit category":
        edit_category(expenses, category_menu )
        save_data(expenses, category_menu)

    elif action == "show graph":
        plot_graph(expenses)

    elif action == "delete":
        delete_expense(expenses)
        save_data(expenses, category_menu)




        