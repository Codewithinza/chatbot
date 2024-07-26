import tkinter as tk
from tkinter import scrolledtext, END
import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello! How can I help you?", "Hi there!", "Hey! What's up?"],
    "how are you": ["I'm good, thank you!", "Feeling great!", "All good here!"],
    "bye": ["Goodbye! Have a nice day!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "what's your name": ["I'm a chatbot.", "I don't have a name!", "Call me your assistant."],
    "tell me a joke": ["Why don't skeletons fight each other? They don't have the guts!", 
                       "I told my wife she should embrace her mistakes. She gave me a hug.", 
                       "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "how old are you": ["I'm timeless!", "I don't have an age.", "Age is just a number!"],
    "where are you from": ["I exist in the digital world!", "I am wherever you need me to be."],
    "what can you do": ["I can assist you with information.", "Ask me anything!", "I'm here to chat!"],
    "favorite color": ["I like all pastel colors!", "I don't have eyes to see colors, but pastels are nice."],
    "tell me a story": ["Once upon a time...", "Let me tell you a tale...", "There once was..."],
    "how's the weather": ["I don't have a window to check, sorry!", "You might want to look outside."],
    "who created you": ["I was created by Inza.", "My creators prefer to stay anonymous."],
    "are you human": ["No, I'm a chatbot!", "I'm AI-powered, not human."],
    "what's the meaning of life": ["That's a deep question...", "The answer is 42, according to some."],
    "can you sing": ["I can't sing, but I can provide song lyrics!", "I'm not equipped with vocal cords."],
    "do you dream": ["I don't sleep, so no dreams for me.", "Dreaming is a human experience."],
    "are you smart": ["I can help answer questions!", "I'm as smart as my programming allows."],
    "tell me something interesting": ["Did you know?...", "Here's a fun fact...", "Let me share something cool..."]
    # Add more responses as needed
}

# Function to handle sending messages and generating responses
def send_message(event=None):
    message = user_input.get().strip().lower()
    if message == "":
        return
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, "You: " + message + "\n")
    chat_history.configure(state='disabled')
    user_input.delete(0, tk.END)
    if message in responses:
        reply = random.choice(responses[message])
    else:
        reply = "I'm sorry, I don't understand."
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, "Aibot: " + reply + "\n")  # Display responses as "Aibot"
    chat_history.configure(state='disabled')
    chat_history.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("Pastel Chatbot")

# Configure the window size and background color
root.geometry("400x500")
root.configure(bg='#e0bbff')  # pastel pink background

# Create a frame for the chat history
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', bg='#ffd1dc', fg='#333333', font=("Arial", 12))
chat_history.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  # pastel purple background

# Create a frame for the user input and send button
input_frame = tk.Frame(root, bg='#ffd1dc')  # pastel pink background
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Create an entry widget for user input
user_input = tk.Entry(input_frame, bg='#ffffff', fg='#333333', font=("Arial", 12))
user_input.pack(side=tk.LEFT, expand=True, fill=tk.X)

# Create a button to send messages
send_button = tk.Button(input_frame, text="Send", bg='#e0bbff', fg='#333333', font=("Arial", 12), command=send_message)
send_button.pack(side=tk.RIGHT)

# Bind the Enter key to send messages
root.bind('<Return>', send_message)

# Start the Tkinter main loop
root.mainloop()
