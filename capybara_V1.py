mood_history = []

def give_advice(mood):
    if mood == "sad":
        return "take a short walk and drink somme water"
    elif mood == "tired":
        return  "sleep early toninght your brain needs a rest"
    elif mood == "happy":
        return "keep doing what made your day"
    elif mood == "angry":
        return "pause,breathe slowly and don't react fast"
    else:
        return"write a short note about your day."

print("capybara v1 ia alive ")

while True:
    mood = input("how do you feel? (happy/n,sad/n,tired/n,angry/n,exit/n)").lower()
    
    if mood == "exit":
        print("goodbye from capybara ")
        break

    mood_history.append(mood)
    print("Advice:", give_advice(mood))
    print("mood history:", mood_history)
    print("-"*30)