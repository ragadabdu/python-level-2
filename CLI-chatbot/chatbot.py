import random, re

responses = {
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "fallback" : ["Can you repeat that", "Hmm, I dont understand", "that's confusing.."]
}

expenses= []

income = 0

balance = 0


while True:
    user = input("what can i help you with: ").lower().strip()
    #words = user.split()
    match = re.search(r"(spent|paid)\s+(\d+)\s+(on|for)\s+(\w+)", user, re.I)
    if match:
        action = match.group(1).lower()
        amount = int(match.group(2))
        category = match.group(4).lower()
        expenses.append({"category": category , "amount": amount})
        balance -= amount
        print(action,amount,category)
        print(f'Bot: You spent {amount} on {category}, got it!')

    elif re.search("bye", user, re.I):
        print(random.choice(responses["farewell"]))
        break

    elif re.search(r"earned|got", user, re.I):
        number = re.findall(r"\d+", user)
        amount = number[0]
        income += int(amount)
        balance += int(amount)
        print(f"Bot: Got it! added income: {amount} ")

    elif re.search(r"balance\b", user, re.I):
        print(f"Bot: Your current balance is: {balance} ")

    elif re.search(r"^(?=.*show)(?=.*expenses)(?=.*category).*$", user, re.I):
        total_amount = {}
        for expense in expenses:
            category = expense["category"]
            total_amount[category] = total_amount.get(category,0) + expense["amount"]
        for category, total in total_amount.items():
            print(f'Bot: You\'ve spent {total} on {category}.')

    elif re.search(r"summary\b", user, re.I):
        total = 0
        for expense in expenses:
            total += int(expense["amount"])

        print(f"Bot: Income: {income} | Expenses: {total} | Balance: {balance}")
        
    else:
        print(random.choice(responses["fallback"]))

