import random
import tkinter as tk

# User database (username: name)
user_db = {}

# Questions database (category: [list of 10 questions])
questions_db = {
'General Knowledge': [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "answer": "Carbon Dioxide"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "George Orwell"],
            "answer": "William Shakespeare"
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        },
        {
            "question": "Who is known as the father of modern physics?",
            "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
            "answer": "Albert Einstein"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "South Korea", "Japan", "Vietnam"],
            "answer": "Japan"
        },
        {
            "question": "What is the chemical symbol for the element gold?",
            "options": ["Go", "Ag", "Au", "Gl"],
            "answer": "Au"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1921", "1907", "1935"],
            "answer": "1912"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Yuan", "Dollar", "Yen", "Won"],
            "answer": "Yen"
        }
    ],
    'Science': [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2", "NaCl"],
            "answer": "H2O"
        },
        {
            "question": "Who is known as the father of modern computer science?",
            "options": ["Alan Turing", "Isaac Newton", "Albert Einstein", "Charles Babbage"],
            "answer": "Alan Turing"
        },
        {
            "question": "What is the process by which plants make their own food?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
            "answer": "Photosynthesis"
        },
        {
            "question": "How many bones are there in the adult human body?",
            "options": ["206", "150", "100", "250"],
            "answer": "206"
        },
        {
            "question": "What is the chemical formula for oxygen?",
            "options": ["O2", "H2O", "CO2", "N2"],
            "answer": "O2"
        },
        {
            "question": "Who discovered the theory of relativity?",
            "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
            "answer": "Albert Einstein"
        },
        {
            "question": "What is the closest star to Earth?",
            "options": ["Sirius", "Proxima Centauri", "Betelgeuse", "Polaris"],
            "answer": "Proxima Centauri"
        },
        {
            "question": "What gas do humans breathe out?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Giraffe", "Blue Whale", "Kangaroo"],
            "answer": "Blue Whale"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Mitochondria", "Ribosome", "Lysosome"],
            "answer": "Mitochondria"
        }
    ],
    'History': [
        {
            "question": "Who was the first President of the United States?",
            "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
            "answer": "George Washington"
        },
        {
            "question": "When was the Declaration of Independence signed?",
            "options": ["1776", "1789", "1801", "1812"],
            "answer": "1776"
        },
        {
            "question": "Who was the leader of the Indian independence movement against British rule?",
            "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Patel"],
            "answer": "Mahatma Gandhi"
        },
        {
            "question": "Which ancient civilization is known for building the Great Wall of China?",
            "options": ["Greek", "Roman", "Egyptian", "Chinese"],
            "answer": "Chinese"
        },
        {
            "question": "Who was the first Emperor of Rome?",
            "options": ["Julius Caesar", "Augustus", "Nero", "Constantine"],
            "answer": "Augustus"
        },
        {
            "question": "What was the period of renewed interest in art and learning in Europe known as?",
            "options": ["Renaissance", "Enlightenment", "Industrial Revolution", "Baroque"],
            "answer": "Renaissance"
        },
        {
            "question": "Who was the last pharaoh of Egypt?",
            "options": ["Cleopatra", "Nefertiti", "Hatshepsut", "Ramses II"],
            "answer": "Cleopatra"
        },
        {
            "question": "In which year did World War I begin?",
            "options": ["1914", "1917", "1918", "1920"],
            "answer": "1914"
        },
        {
            "question": "Who is famous for his voyages to the Americas in 1492?",
            "options": ["Christopher Columbus", "Amerigo Vespucci", "Ferdinand Magellan", "Marco Polo"],
            "answer": "Christopher Columbus"
        },
        {
            "question": "Who wrote 'The Art of War,' an ancient Chinese military treatise?",
            "options": ["Sun Tzu", "Confucius", "Laozi", "Mencius"],
            "answer": "Sun Tzu"
        }
    ],
    'Programming': [
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Transfer Markup Language", "Hyper Text Makeup Language", "Hyper Text Markup Language", "High Tech Modern Language"],
            "answer": "Hyper Text Markup Language"
        },
        {
            "question": "Which programming language is known for its use in web development?",
            "options": ["Python", "Java", "C++", "JavaScript"],
            "answer": "JavaScript"
        },
        {
            "question": "What does 'CSS' stand for in web development?",
            "options": ["Cascading Style Sheets", "Computer Style System", "Creative Style Selector", "Colorful Style Sheet"],
            "answer": "Cascading Style Sheets"
        },
        {
            "question": "What is the main function of a version control system like Git?",
            "options": ["Debugging Code", "Creating Databases", "Managing Project Versions", "Running Web Servers"],
            "answer": "Managing Project Versions"
        },
        {
            "question": "What is the term for a named storage location in a program?",
            "options": ["Variable", "Command", "Statement", "Function"],
            "answer": "Variable"
        },
        {
            "question": "What is the most widely used programming language for artificial intelligence?",
            "options": ["Python", "Java", "C++", "Ruby"],
            "answer": "Python"
        },
        {
            "question": "Which company developed the Python programming language?",
            "options": ["Google", "Apple", "Microsoft", "Facebook"],
            "answer": "Google"
        },
        {
            "question": "What does 'IDE' stand for in the context of software development?",
            "options": ["Integrated Development Environment", "Interactive Design Environment", "Internet Development Environment", "Independent Design Engine"],
            "answer": "Integrated Development Environment"
        },
        {
            "question": "What is the process of finding and fixing errors in a program called?",
            "options": ["Testing", "Debugging", "Compiling", "Coding"],
            "answer": "Debugging"
        },
        {
            "question": "What is the term for a software program that is harmful and spreads to other computers?",
            "options": ["Virus", "Spyware", "Firewall", "Encryption"],
            "answer": "Virus"
        }
    ]}

# Scoreboard (username: score)
scoreboard = {}

current_user = None  # To store the current user

def register_user():
    username = username_entry.get()
    if username:
        user_db[username] = username
        scoreboard[username] = 0
        username_entry.delete(0, 'end')
        result_label.config(text=f"User '{username}' registered successfully.")
    else:
        result_label.config(text="Please enter a valid name.")

def login_user():
    global current_user
    name = username_entry.get()
    if name in user_db:
        current_user = name
        username_entry.delete(0, 'end')
        result_label.config(text=f"Login successful, {current_user}.")
    else:
        result_label.config(text="Name not found. Please register first.")

def start_quiz():
    if current_user:
        selected_category = category_var.get()
        if selected_category in questions_db:
            questions = questions_db[selected_category]
            random.shuffle(questions)
            user_score = 0
            for question in questions[:10]:
                question_text = question["question"]
                options = question["options"]
                correct_answer = question["answer"]
                user_answer = ask_question(question_text, options)
                if user_answer == correct_answer:
                    user_score += 1
            scoreboard[current_user] = user_score
            result_label.config(text=f"Quiz completed. Your score: {user_score} points.")
        else:
            result_label.config(text="Invalid category choice.")
    else:
        result_label.config(text="Please login first.")

def ask_question(question_text, options):
    question_window = tk.Toplevel(root)
    question_window.title("Question")
    question_label = tk.Label(question_window, text=question_text)
    question_label.pack()
    answer_var = tk.StringVar()
    for i, option in enumerate(options, start=1):
        option_radio = tk.Radiobutton(question_window, text=option, variable=answer_var, value=option)
        option_radio.pack()
    submit_button = tk.Button(question_window, text="Submit", command=question_window.destroy)
    submit_button.pack()
    question_window.wait_window(question_window)
    return answer_var.get()

def display_scoreboard():
    sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    scoreboard_window = tk.Toplevel(root)
    scoreboard_window.title("Scoreboard")
    scoreboard_label = tk.Label(scoreboard_window, text="Scoreboard")
    scoreboard_label.pack()
    for i, (username, score) in enumerate(sorted_scores, start=1):
        score_label = tk.Label(scoreboard_window, text=f"{i}. {username}: {score} points")
        score_label.pack()

# Create the main GUI window
root = tk.Tk()
root.title("Quiz Application")

# Create and configure GUI components
username_label = tk.Label(root, text="Enter your name:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

login_button = tk.Button(root, text="Login", command=login_user)
login_button.pack()

category_label = tk.Label(root, text="Select a category:")
category_label.pack()

categories = list(questions_db.keys())
category_var = tk.StringVar(root)
category_var.set(categories[0])
category_optionmenu = tk.OptionMenu(root, category_var, *categories)
category_optionmenu.pack()

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

scoreboard_button = tk.Button(root, text="Display Scoreboard", command=display_scoreboard)
scoreboard_button.pack()

# Start the GUI main loop
root.mainloop()
