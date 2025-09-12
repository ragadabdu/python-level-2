import random

responses = {
    "greeting" : ["Hello, friend!", "Hi, how ya doinn", "Hey there"],
    "answers" : ["the solution is xxx", "I will look this up now..."],
    "fallback" : ["Can you repeat that", "Hmm, I dont understand", "that's confusing.."]
}

while True:
    user = input("Say something: ").lower().strip()
    words = user.split()

    if any(word in ["hello", "hi", "hey"] for word in words):
        print(random.choice(responses["greeting"]))
    
    elif any(word in ["what", "when", "does"] for word in words):
        print(random.choice(responses["answers"]))
    
    elif user == "quit":
        print("That's it, see you.")
        break

    else:
        print(random.choice(responses["fallback"]))

