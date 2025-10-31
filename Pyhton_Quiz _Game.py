# Pyhton Quiz Game using Tkinter

import tkinter as tk
from tkinter import messagebox
import random

questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pyth", ".pt", ".pyt", ".py"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def"
    },
    {
        "question": "What is the output of print(2**3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "List"
    },
    {
        "question": "What will be the output of len('Python')?",
        "options": ["5", "6", "7", "Error"],
        "answer": "6"
    },
    {
        "question": "Which of the following is used to comment a single line in Python?",
        "options": ["#", "//", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "What will be the output of print(type([]))?",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'set'>", "<class 'dict'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which built-in function is used to get the length of a list in Python?",
        "options": ["count()", "len()", "size()", "length()"],
        "answer": "len()"
    },
    {
        "question": "What is the output of print(10//3)?",
        "options": ["3", "3.33", "3.0", "Error"],
        "answer": "3"
    }
]

random.shuffle(questions)

root = tk.Tk()
root.title("🤖 AI Quiz Game")
root.geometry("500x400")
root.config(bg="#F3F3F3")

score = 0
q_index = 0
selected_option = tk.StringVar()

def show_question():
    global q_index
    question_label.config(text=questions[q_index]["question"])
    selected_option.set(None)
    for i in range(4):
        option_buttons[i].config(text=questions[q_index]["options"][i], value=questions[q_index]["options"][i])

def check_answer():
    global score, q_index
    chosen = selected_option.get()
    correct = questions[q_index]["answer"]

    if chosen == correct:
        score += 1
        messagebox.showinfo("Result", "✅ Correct!")
    else:
        messagebox.showwarning("Result", f"❌ Wrong!\nCorrect Answer: {correct}")

    q_index += 1
    if q_index < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    result_text = f"Your final score is {score}/{len(questions)}"
    if score == len(questions):
        msg = "🏆 Excellent! You are an AI Genius!"
    elif score >= len(questions)/2:
        msg = "👍 Good Job! You know quite a bit!"
    else:
        msg = "😅 Keep learning about AI!"
    messagebox.showinfo("Quiz Over", result_text + "\n" + msg)
    root.destroy()

title_label = tk.Label(root, text="🤖 AI Quiz Game", font=("Arial", 18, "bold"), bg="#F3F3F3", fg="#2E2E2E")
title_label.pack(pady=20)

question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 14), bg="#F3F3F3")
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected_option, value="", font=("Arial", 12), bg="#F3F3F3", anchor="w", indicatoron=0, width=30)
    btn.pack(pady=5)
    option_buttons.append(btn)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20)
submit_button.pack(pady=20)

show_question()
root.mainloop()
