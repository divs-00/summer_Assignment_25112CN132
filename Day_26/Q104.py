"""
PROBLEM STATEMENT:
Write a program to Create quiz application.
"""

def run_quiz(quiz_data):

    """Runs an interactive quiz application based on the provided question data.
       This function iterates through questions, handles user input validation, 
       tracks the score, and provides a final performance summary.
       The time complexity of running the quiz is O(n), where n is the number of questions."""
    
    score = 0
    
    print("Welcome to the Quiz Application!")
    
    print("Please answer by entering the letter of your choice (A, B, C, or D).\n")
    
    for index, q in enumerate(quiz_data, 1):
    
        print(f"Question {index}: {q['question']}")
        
        for option, text in q['options'].items():
        
            print(f"{option}. {text}")
            
        while True:
        
            user_answer = input("Your answer: ").strip().upper()
            
            if user_answer in ['A', 'B', 'C', 'D']:
            
                break
                
            print("Invalid choice. Please enter A, B, C, or D.")
            
        if user_answer == q['answer']:
        
            print("Correct!\n")
            
            score += 1
            
        else:
        
            print(f"Wrong. The correct answer was {q['answer']}: {q['options'][q['answer']]}\n")
            
    print("--- Quiz Results ---")
    
    print(f"Your final score is {score} out of {len(quiz_data)}.")

questions = [

    {
        "question": "What is the correct file extension for Python files?",
        "options": {"A": ".pt", "B": ".py", "C": ".pyt", "D": ".pyw"},
        "answer": "B"
    },
    
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "define", "C": "def", "D": "function"},
        "answer": "C"
    },
    
    {
        "question": "Which data type is used to store multiple items in a single variable, ordered and unchangeable?",
        "options": {"A": "List", "B": "Set", "C": "Dictionary", "D": "Tuple"},
        "answer": "D"
    }
    
]

run_quiz(questions)