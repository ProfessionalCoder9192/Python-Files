import sys
import time
import random
import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama console system
colorama.init(autoreset=True)

def typewriter_print(text, color_prefix="", delay=0.015):
    """Prints text character by character to create an animated typewriter effect."""
    sys.stdout.write(color_prefix)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def get_bot_response(sentiment_score):
    """Selects a contextually appropriate reply based on the calculated numeric score."""
    # Positive responses (Polarity > 0.15)
    positive_replies = [
        "That sounds wonderful! I am so glad to hear that. 😊",
        "Awesome! Your energy is absolutely fantastic right now.🚀",
        "That's great! Keep holding onto that great vibe.",
        "How wonderful! Tell me more about what's making you happy!"
    ]
    
    # Negative responses (Polarity < -0.15)
    negative_replies = [
        "I am really sorry to hear that. I'm here if you want to vent. 😔",
        "That sounds incredibly tough. Take a deep breath, you've got this.",
        "Oh no, I'm sorry things are feeling heavy right now. 🌧️",
        "That sounds frustrating. I'm here to listen if you want to talk it through."
    ]
    
    # Neutral responses (-0.15 <= Polarity <= 0.15)
    neutral_replies = [
        "I see. Fascinating perspective! Tell me more about it. 💬",
        "Got it. Thanks for sharing that with me.",
        "Interesting! What else is on your mind today?",
        "I hear you. Let's keep exploring that topic."
    ]
    
    if sentiment_score > 0.15:
        return random.choice(positive_replies)
    elif sentiment_score < -0.15:
        return random.choice(negative_replies)
    else:
        return random.choice(neutral_replies)

# --- Core Interaction Loop ---
print(f"{Fore.CYAN}{Style.BRIGHT}===============================================")
print(f"{Fore.CYAN}{Style.BRIGHT}        SENTIMENT-AWARE CHATBOT INITIALIZED    ")
print(f"{Fore.CYAN}{Style.BRIGHT}===============================================")
typewriter_print("Hello! I am a chatbot that pays close attention to your mood.", Fore.MAGENTA)
typewriter_print("Type anything on your mind, or type 'exit' or 'quit' to end our chat.\n", Fore.MAGENTA)

while True:
    # 1. Capture User Input
    user_input = input(f"{Fore.WHITE}{Style.BRIGHT}You: ").strip()
    
    # Check escape command triggers
    if user_input.lower() in ['exit', 'quit']:
        print(f"\n{Fore.MAGENTA}===============================================")
        typewriter_print("Goodbye! Thanks for chatting with me today. Take care! 👋", Fore.MAGENTA)
        break
        
    if not user_input:
        typewriter_print("You didn't say anything! Don't be shy.", Fore.YELLOW)
        continue
        
    # 2. TextBlob Analytical Polarity Metrics Calculation
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity  # Returns a score floating between -1.0 and 1.0
    
    # 3. Establish Interface Color Mappings
    if polarity > 0.15:
        mood_label = "POSITIVE"
        tracker_color = Fore.GREEN
    elif polarity < -0.15:
        mood_label = "NEGATIVE"
        tracker_color = Fore.RED
    else:
        mood_label = "NEUTRAL"
        tracker_color = Fore.YELLOW
        
    # 4. Render Analytical Live Telemetry Data Card
    print(f"{Style.DIM}  [Tracker System: Detected {tracker_color}{mood_label}{Style.RESET_ALL}{Style.DIM} mood | Polarity Score: {polarity:+.2f}]")
    
    # 5. Type Out the Selected Bot Response Matrix Row
    reply = get_bot_response(polarity)
    sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}Bot: ")
    sys.stdout.flush()
    typewriter_print(reply, tracker_color)
    print() # Formatting spacer line
