import random

while True:
    user = input("Say something: ").lower()
    if (user == "hello" or user == "hi" or user == "hey there"):
        reply = ["hi", "heyy!"]
        response = random.choice(reply)
        print(response)
    
    elif (user == "how are you?" or user == "how are you doing?" or user == "how are you" or user == "How are you doing"):
        reply = ["Fine, what about you", "Great, how are you"]
        response = random.choice(reply)
        print(response)
    
    else:
        print("Oh, I dont know how to respond")

