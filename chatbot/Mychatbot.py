#.................................................CHATBOT...................................................................

import random

# Define the chatbot's responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm here to help!", "I don't have feelings, but thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "morning": ["Good Morning! Have a nice day", "Morning"],
    "thanks": ["Your Welcome!", "Its my Plasure"],
    "good night": ["Good Night!", "Take Care!","Good Night, Sweet dreams!"],
    "Are you human ?": ["No! I'm a bot", "No! I'm a Robot"],
    "Are you robot ?":  ["yes! I'm  a Robot"]

}

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    
    return "I'm sorry, I don't understand that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)



