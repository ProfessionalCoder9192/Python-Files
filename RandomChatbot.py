import sys
import time
import colorama
from colorama import Fore, Style

# Initialize colorama console system
colorama.init(autoreset=True)

def typewriter_print(text, color_prefix="", delay=0.012):
    """Prints text character by character to simulate a typewriter interface."""
    sys.stdout.write(color_prefix)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def show_menu():
    """Prints clear shortcut numbers and options using clean styling rules."""
    print(f"\n{Fore.GREEN}{Style.BRIGHT}--- CHATBOT MODULE INDEX ---")
    print(f"  [{Fore.YELLOW}1{Fore.WHITE}] Check Local Temperature")
    print(f"  [{Fore.YELLOW}2{Fore.WHITE}] View Current Global News")
    print(f"  [{Fore.YELLOW}3{Fore.WHITE}] Re-print This Option Menu")
    print(f"  [{Fore.YELLOW}4{Fore.WHITE}] Close the Chatbot Panel")
    print("-" * 28 + "\n")

# --- Initial Greeting Sequence ---
print(f"{Fore.CYAN}{Style.BRIGHT}===============================================")
print(f"{Fore.CYAN}{Style.BRIGHT}        INDEX-ROUTED UTILITY CHATBOT          ")
print(f"{Fore.CYAN}{Style.BRIGHT}===============================================")
typewriter_print("System active. Please input a numerical selection to query data.", Fore.MAGENTA)
show_menu()

# --- Continuous Main Interaction Loop ---
while True:
    user_input = input(f"{Fore.WHITE}{Style.BRIGHT}You (Enter 1-4): ").strip()
    
    if not user_input:
        continue
        
    # Router conditional block logic matching numeric index values
    if user_input == "1":
        sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}Bot: ")
        sys.stdout.flush()
        typewriter_print("Fetching regional climate and temperature tracking telemetry...", Fore.GREEN)
        
        print(f"\n{Fore.YELLOW}🌡️  ENVIRONMENT STATUS REPORT:")
        print(f"  • Current Temp : {Fore.WHITE}72°F / 22°C")
        print(f"  • Humidity     : {Fore.WHITE}45%")
        print(f"  • Condition    : {Fore.WHITE}Clear Skies & Sunny")
        print(f"  • Status       : {Fore.GREEN}Optimal Climate Matrix\n")
        
    elif user_input == "2":
        sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}Bot: ")
        sys.stdout.flush()
        typewriter_print("Retrieving the latest news feeds...", Fore.GREEN)
        
        print(f"\n{Fore.MAGENTA}📰 CURRENT GLOBAL HEADLINES [2026 Updates]:")
        print(f"  1. {Fore.WHITE}International trade routes shift following new clean-energy maritime regulations.")
        print(f"  2. {Fore.WHITE}Record-breaking heatwave prompts cities to implement new smart grid cooling strategies.")
        print(f"  3. {Fore.WHITE}Sports spotlight: Defending soccer champions secure a dominant 3-1 win to progress.")
        print(f"  4. {Fore.WHITE}Next-gen computing architectures drastically scale back energy use in large logistics networks.\n")
        
    elif user_input == "3":
        show_menu()
        
    elif user_input == "4" or user_input.lower() in ['exit', 'quit']:
        print(f"\n{Fore.MAGENTA}===============================================")
        typewriter_print("Disconnecting from all modules. Goodbye! 🍿", Fore.MAGENTA)
        break
        
    else:
        # Standard conversation fallback if they don't enter an index option
        sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}Bot: ")
        sys.stdout.flush()
        typewriter_print(f"Unrecognized number. Please enter {Fore.YELLOW}1{Fore.CYAN} for temp, {Fore.YELLOW}2{Fore.CYAN} for news, or {Fore.YELLOW}3{Fore.CYAN} to view options.", Fore.YELLOW)
        print()
