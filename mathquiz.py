import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer

def run_quiz():
    print("Welcome to the Simple Math Quiz!")
    score = 0

    for i in range(5): 
        question, correct_answer = generate_question()
        print(f"Q{i+1}: {question} = ?")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer was {correct_answer}\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print(f"Quiz Over! You got {score} out of 5 right.")

if __name__ == "__main__":
    run_quiz()
