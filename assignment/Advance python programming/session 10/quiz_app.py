import tkinter as tk

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Jaipur", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which is the longest river in India?",
        "options": ["Yamuna", "Godavari", "Ganga", "Narmada"],
        "answer": "Ganga"
    },
    {
        "question": "Which is the largest Indian state by area?",
        "options": ["Gujarat", "Rajasthan", "Maharashtra", "Punjab"],
        "answer": "Rajasthan"
    },
    {
        "question": "Which desert is in Rajasthan?",
        "options": ["Sahara", "Thar", "Gobi", "Kalahari"],
        "answer": "Thar"
    },
    {
        "question": "Which ocean is south of India?",
        "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "answer": "Indian"
    }
]

state = {"index": 0, "score": 0}

def check(option):
    if option == questions[state["index"]]["answer"]:
        result_label.config(text="Correct!")
        state["score"] += 1
    else:
        result_label.config(text="Wrong!")

    for button in option_buttons:
        button.config(state="disabled")

def next_question():
    state["index"] += 1

    if state["index"] < 5:
        question_label.config(text=questions[state["index"]]["question"])
        result_label.config(text="")

        for i, option in enumerate(questions[state["index"]]["options"]):
            option_buttons[i].config(
                text=option,
                state="normal",
                command=lambda option=option: check(option)
            )
    else:
        question_label.config(text="Your score: " + str(state["score"]) + "/5")

        for button in option_buttons:
            button.grid_remove()

        result_label.config(text="")
        next_button.grid_remove()
        restart_button.grid(row=5, column=0, columnspan=2, pady=10)

    score_label.config(text="Score: " + str(state["score"]))

def restart():
    state["index"] = 0
    state["score"] = 0

    question_label.config(text=questions[0]["question"])
    score_label.config(text="Score: 0")
    result_label.config(text="")

    for i, option in enumerate(questions[0]["options"]):
        option_buttons[i].config(text=option, state="normal")
        option_buttons[i].grid(row=2 + i // 2, column=i % 2)

    restart_button.grid_remove()
    next_button.grid(row=5, column=1)

root = tk.Tk()
root.title("Indian Geography Quiz")
root.geometry("450x350")

heading = tk.Label(root, text="Indian Geography Quiz", font=("Arial", 18))
heading.grid(row=0, column=0, columnspan=2, pady=15)

question_label = tk.Label(root, text=questions[0]["question"], font=("Arial", 12))
question_label.grid(row=1, column=0, columnspan=2, pady=10)

option_buttons = []

for i, option in enumerate(questions[0]["options"]):
    button = tk.Button(root, text=option, command=lambda option=option: check(option))
    button.grid(row=2 + i // 2, column=i % 2, padx=10, pady=10)
    option_buttons.append(button)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.grid(row=5, column=0, pady=10)

next_button = tk.Button(root, text="Next", command=next_question)
next_button.grid(row=5, column=1)

restart_button = tk.Button(root, text="Restart", command=restart)

root.mainloop()