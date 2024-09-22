from tkinter import *
import re
import random

# Define chatbot patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today?",]],
    [r"hi|hello|hey|hiii", ["Hello..! My name is ChatBot.", "Hi there!",]],
    [r"what is your name ?|what is your name", ["My name is ChatBot.",]],
    [r"how are you ?|how are you", ["I'm doing good. How about you?",]],
    [r"sorry", ["It's ok, don't worry about it."]],  # Specific response for "sorry"
    [r"i am good|I am well|I am okay|I am ok", ["Nice to hear that.",]],
    [r"(.*) age?", ["I'm a computer program, I don't have an age.",]],
    [r"quit", ["Bye! Take care.", "Goodbye!", "See you later!"]],
    [r"bye", ["Goodbye! It was nice chatting with you. Have a great day!"]],
    [r"thanks", ["You're welcome!"]],
    [r"i love you|than i hate you", ["I don't have any feelings."]],
    [r"(.*)", ["I'm not sure I understand that.", "Could you please clarify?", "Tell me more about that."]]
]

# Reflections for basic transformations
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",

    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define chatbot logic
def respond_to_input(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    for pattern, responses in pairs:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            # Apply reflections
            for key, value in reflections.items():
                response = re.sub(r"\b" + re.escape(key) + r"\b", value, response)
            return response % match.groups()
    return "I'm not sure I understand that."

def send_message():
    user_input = user_entry.get()
    if user_input:
        task_listbox.insert(END, "You: " + user_input)
        response = respond_to_input(user_input)
        task_listbox.insert(END, "ChatBot: " + response)
        task_listbox.insert(END, "")  # Insert a blank line for separation
        user_entry.delete(0, END)
        task_listbox.yview(END)  # Auto-scroll to the bottom

def exit_app():
    root.destroy()  # Properly close the Tkinter window

# Initialize the main window
root = Tk()
root.config(bg="white")
root.geometry("1550x900")
root.title("CHATTING APP")
root.resizable(False, False)
canvas = Canvas(root,width=658,height=551)
canvas.config(bg ='black')
canvas.place(x=445,y=6)


# Define font for Listbox
listbox_font = ("Helvetica", 14)  # Adjust font family and size

# Define UI components
task_listbox = Listbox(root, width=58, height=21, selectmode=SINGLE, bg="LIGHT GRAY", fg="blue", borderwidth=0, font=listbox_font)
task_listbox.place(x=449, y=72)

scrollbar = Scrollbar(root)
scrollbar.place(x=1086, y=72, height=485)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Define font for Entry and Button widgets
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12)

canvas = Canvas(root,width=652,height=32)
canvas.config(bg ='black')
canvas.place(x=446,y=597)

user_entry = Entry(root, width=72, bg="Light gray", fg="#333", borderwidth=0, font=entry_font)
user_entry.place(x=449, y=600, height=30)

label = Label(root, text = "BASIC CHATBOT",font = entry_font,bg="light blue",fg = "black", width=72,height=3)
label.place(x=449,y=10)

canvas = Canvas(root,width=323,height=30)
canvas.config(bg ='black')
canvas.place(x=775,y=634)

send_button = Button(root, text="Send", command=send_message, bg="#90EE90", width=35, font=button_font, borderwidth=0)
send_button.place(x=778, y=637)

canvas = Canvas(root,width=323,height=30)
canvas.config(bg ='black')
canvas.place(x=446,y=634)

exit_button = Button(root, text="Exit", command=exit_app, bg="red", width=35, font=button_font, borderwidth=0)
exit_button.place(x=449, y=637)
root.config(bg="white")


root.mainloop()
