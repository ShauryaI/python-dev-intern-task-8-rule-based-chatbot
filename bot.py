def chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! I can respond to 'hello', 'how are you', and 'bye'. What would you like to know?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop for interaction
while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        print("Chatbot: Exiting conversation.")
        break
    response = chatbot(user_message)
    print(f"Chatbot: {response}")