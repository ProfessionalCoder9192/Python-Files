import random

questions = [
    {
        "question": "What does 'len()' do?",
        "options": ["Adds numbers", "Finds length", "Creates list", "Stops loop"],
        "answer": "Finds length"
    },
    {
        "question": "Symbol for multiplication in Python?",
        "options": ["x", "*", "×", "/"],
        "answer": "*"
    },
    {
        "question": "Keyword to define a function?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Module to generate random numbers?",
        "options": ["random", "math", "numbers", "os"],
        "answer": "random"
    },
    {
        "question": "Output of: print(3 * 2)?",
        "options": ["5", "6", "8", "9"],
        "answer": "6"
    },
]

def run_quiz():
    score = 0
    for q in random.sample(questions, 3):
        print(q["question"])
        opts = q["options"]
        random.shuffle(opts)
        for i, opt in enumerate(opts):
            print(f"{i+1}. {opt}")
        try:
            ans = int(input("Your answer: "))
            if opts[ans - 1] == q["answer"]:
                score += 1
        except:
            pass
        print()

    print(f"Your score: {score}/3")

if __name__ == "__main__":
    run_quiz()