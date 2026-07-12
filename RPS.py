import sys
import time
import random
import colorama
from colorama import Fore, Back, Style

# Initialize colorama console system
colorama.init(autoreset=True)

# --- Stylized ASCII Hand Designs ---
ROCK = f"""
    {Fore.YELLOW}_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = f"""
    {Fore.CYAN}_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = f"""
    {Fore.MAGENTA}_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

HANDS = {"1": ROCK, "2": PAPER, "3": SCISSORS}
NAMES = {"1": "ROCK", "2": "PAPER", "3": "SCISSORS"}

def clear_and_header():
    """Clears the terminal scroll space to draw a clean UI panel frame."""
    print("\n" * 30) # Clear terminal illusion for universal support
    print(f"{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}==================================================")
    print(f"{Back.BLUE}{Fore.WHITE}{Style.BRIGHT} 💥   ULTIMATE ROCK-PAPER-SCISSORS SHOWDOWN   💥 ")
    print(f"{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}==================================================")

def draw_health_bar(player_name, health, max_health=3, bar_color=Fore.GREEN):
    """Generates an arcade style glowing health bar layout."""
    hearts = "❤️ " * health
    empty = "🖤 " * (max_health - health)
    bar_segments = "█" * health + "░" * (max_health - health)
    print(f"{Fore.WHITE}{Style.BRIGHT}{player_name:<10} [{bar_color}{bar_segments}{Fore.WHITE}] {hearts}{empty}")

def animated_announcement(text, text_color=Fore.CYAN):
    """Flashes a dramatic banner out onto the display center."""
    print(f"\n{text_color}{Style.BRIGHT}>>> {text.upper()} <<<")
    time.sleep(0.4)

def run_dramatic_countdown():
    """Flashes a professional high-speed fighting-game countdown loop."""
    print(f"\n{Fore.WHITE}{Style.BRIGHT}Get Ready... ", end="")
    sys.stdout.flush()
    time.sleep(0.4)
    
    countdowns = [f"{Fore.YELLOW}ROCK!", f"{Fore.CYAN}PAPER!", f"{Fore.MAGENTA}SCISSORS!", f"{Fore.RED}{Style.BRIGHT}SHOOT!!!\n"]
    for word in countdowns:
        sys.stdout.write(word + "  ")
        sys.stdout.flush()
        time.sleep(0.35)
    print("\n")

# --- Core Game Initialization State ---
p_health = 3
c_health = 3
round_num = 1

clear_and_header()
print(f"\n{Fore.GREEN}🕹️ Welcome Hero! First fighter to drop to 0 health loses.")
print(f"{Fore.WHITE}Make your choices carefully. Good luck!\n")
input(f"{Fore.CYAN}Press [ENTER] to ignite the arena battlefield...")

# --- Continuous Main Arcade Fight Loop ---
while p_health > 0 and c_health > 0:
    clear_and_header()
    print(f"\n{Fore.CYAN}{Style.BRIGHT}⚡ ROUND {round_num} ⚡\n")
    
    # Render tracking telemetry health displays
    draw_health_bar("PLAYER", p_health, bar_color=Fore.GREEN)
    draw_health_bar("BOT-9000", c_health, bar_color=Fore.RED)
    print(f"{Fore.WHITE}-" * 50)
    
    # Input selection validation block
    print(f"\n{Fore.WHITE}Choose your weapon index:")
    print(f" [{Fore.YELLOW}1{Fore.WHITE}] {Fore.YELLOW}ROCK")
    print(f" [{Fore.CYAN}2{Fore.WHITE}] {Fore.CYAN}PAPER")
    print(f" [{Fore.MAGENTA}3{Fore.WHITE}] {Fore.MAGENTA}SCISSORS")
    
    player_choice = input(f"\n{Fore.WHITE}{Style.BRIGHT}Select weapon (1-3) or 'exit': ").strip()
    
    if player_choice.lower() in ['exit', 'quit']:
        print(f"\n{Fore.MAGENTA}Fleeing the battlefield? Game over!")
        break
        
    if player_choice not in ['1', '2', '3']:
        animated_announcement("Invalid input! Focus up warrior!", Fore.RED)
        continue
        
    # Generate bot opponent choice value
    bot_choice = random.choice(['1', '2', '3'])
    
    # Execute cinematic visual clock countdown 
    run_dramatic_countdown()
    
    # Draw side-by-side combat graphics layout
    print(f"{Fore.GREEN}{Style.BRIGHT}YOUR CHOICE: {NAMES[player_choice]}")
    print(HANDS[player_choice])
    print(f"{Fore.RED}{Style.BRIGHT}BOT-9000 CHOICE: {NAMES[bot_choice]}")
    print(HANDS[bot_choice])
    print(f"{Fore.WHITE}-" * 50)
    
    # Process outcome conditions matrices
    if player_choice == bot_choice:
        animated_announcement("CLASH! It's a dead lock draw!", Fore.YELLOW)
    elif (player_choice == "1" and bot_choice == "3") or \
         (player_choice == "2" and bot_choice == "1") or \
         (player_choice == "3" and bot_choice == "2"):
        animated_announcement("CRITICAL HIT! You damaged the bot!", Fore.GREEN)
        c_health -= 1
    else:
        # Mini terminal shake simulation illusion
        print("\a", end="") # Plays system alert beep tone
        animated_announcement("OUCH! You took a heavy hit!", Fore.RED)
        p_health -= 1
        
    round_num += 1
    input(f"\n{Fore.WHITE}Press [ENTER] to push forward to next stage...")

# --- Epic Conclusion Finale Screen ---
clear_and_header()
print(f"\n{Fore.CYAN}{Style.BRIGHT}📊 FINAL MATCH OVERVIEW STATISTICS:")
print(f" Total Rounds Lasted: {round_num - 1}")

if p_health > 0:
    print(f"\n{Back.GREEN}{Fore.WHITE}{Style.BRIGHT}  🏆 CONGRATULATIONS! YOU DESTROYED BOT-9000! 🏆  ")
    print(f"{Fore.GREEN}Your remaining health: {p_health}/3")
else:
    print(f"\n{Back.RED}{Fore.WHITE}{Style.BRIGHT}  💀 DEFEAT! BOT-9000 OVERLOADED YOUR SYSTEM! 💀  ")
    print(f"{Fore.RED}Bot remaining health: {c_health}/3")

print(f"\n{Fore.BLUE}==================================================\n")
