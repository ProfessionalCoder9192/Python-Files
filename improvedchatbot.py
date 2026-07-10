import random
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)


def typing_print(text, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def get_user_input():
    sys.stdout.write(Fore.CYAN + "You: " + Style.RESET_ALL)
    return input().strip().lower()


def chatbot():
    typing_print(
        "Chatbot: Hello! I am your AI companion.", Fore.GREEN + Style.BRIGHT
    )
    time.sleep(0.5)
    typing_print("Chatbot: How is your day going so far?", Fore.GREEN)

    user_response = get_user_input()

    positive_words = ["good", "great", "awesome", "fine", "amazing", "happy"]
    negative_words = ["bad", "terrible", "sad", "rough", "exhausting", "tired"]

    if any(word in user_response for word in positive_words):
        typing_print(
            "Chatbot: That is wonderful to hear! I hope it gets even better! 🎉",
            Fore.GREEN,
        )
    elif any(word in user_response for word in negative_words):
        typing_print(
            "Chatbot: I am sorry to hear that. I hope things turn around for you soon. ❤️",
            Fore.YELLOW,
        )
    else:
        typing_print(
            "Chatbot: Thanks for sharing! Every day brings something new.",
            Fore.GREEN,
        )

    time.sleep(0.5)
    typing_print(
        "Chatbot: Is there anything specific you would like to talk about?",
        Fore.GREEN,
    )

    while True:
        user_response = get_user_input()

        if user_response in ["exit", "quit", "bye", "goodbye"]:
            typing_print(
                "Chatbot: Goodbye! Have a fantastic rest of your day! 👋",
                Fore.RED + Style.BRIGHT,
            )
            break

        responses = [
            "Tell me more about that!",
            "That sounds interesting.",
            "I see! What makes you say that?",
            "How does that make you feel?",
        ]
        typing_print("Chatbot: " + random.choice(responses), Fore.GREEN)


if __name__ == "__main__":
    try:
        chatbot()
    except KeyboardInterrupt:
        print()
        typing_print("\nChatbot: Session ended abruptly. Goodbye!", Fore.RED)
