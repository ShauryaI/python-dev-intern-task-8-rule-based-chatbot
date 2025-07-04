import tkinter as tk
from tkinter import scrolledtext
import re

# Create the main window
root = tk.Tk()
root.title("Rule Based Chatbot")

def send_message():
    message = entry_field.get()
    if message:
        chat_history.configure(state='normal')  # Enable editing
        chat_history.insert(tk.END, "You: " + message + "\n")
        reply = get_response(message)
        chat_history.insert(tk.END, "Bot: " + reply + "\n")
        chat_history.configure(state='disabled') # Disable editing
        entry_field.delete(0, tk.END)

# Frame for chat history
messages_frame = tk.Frame(root)
messages_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Chat history display (ScrolledText for scrolling)
chat_history = scrolledtext.ScrolledText(messages_frame, wrap=tk.WORD, state='disabled', width=50, height=15)
chat_history.pack(expand=True, fill="both")

# Entry field for typing messages
entry_field = tk.Entry(root, width=40)
entry_field.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
entry_field.bind("<Return>", lambda event=None: send_message()) # Bind Enter key

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# --- Grid Configuration ---
root.grid_rowconfigure(0, weight=1)  # Make chat history area expandable vertically
root.grid_columnconfigure(0, weight=1) # Make entry field expandable horizontally

rules = {
    "hello|hi|hey": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm a bot, so I don't have feelings, but I'm functioning perfectly!", "I'm doing great, thanks for asking!"],
    "your name": ["I am a rule-based chatbot.", "You can call me Chatbot."],
    "bye|exit|quit": ["Goodbye!", "See you later!", "Have a great day!"],
    ".*": ["I'm sorry, I don't understand that.", "Could you please rephrase?", "I'm still learning, please try another query."]
}

def get_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for case-insensitive matching
    for pattern, responses_list in rules.items():
        if re.search(pattern, user_input):
            import random
            return random.choice(responses_list)
    return "I'm not sure how to respond to that."  # Default fallback

def chat():
    root.mainloop()

if __name__ == "__main__":
    chat()

