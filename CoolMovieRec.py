import sys
import time
import pandas as pd
import colorama
from colorama import Fore, Style

# Initialize colorama console system
colorama.init(autoreset=True)

# 1. Load the dataset
try:
    df = pd.read_csv('imdb_top_1000.csv')
    df.columns = df.columns.str.strip().str.title()
except FileNotFoundError:
    print(f"{Fore.RED}Error: 'imdb_top_1000.csv' not found. Put it in this current folder.")
    exit()

# Map expected dataset variations (using 'Certificate' for age ratings)
title_col = next((c for c in ['Series_Title', 'Title', 'Movie_Title'] if c in df.columns), 'Title')
overview_col = next((c for c in ['Overview', 'Description', 'Plot'] if c in df.columns), 'Overview')
genre_col = next((c for c in ['Genre', 'Genres'] if c in df.columns), 'Genre')
age_col = next((c for c in ['Certificate', 'Age_Rating', 'Rating'] if c in df.columns), 'Certificate')

df[overview_col] = df[overview_col].fillna("").astype(str)
df[title_col] = df[title_col].fillna("Unknown Title").astype(str)
df[genre_col] = df[genre_col].fillna("N/A").astype(str)
df[age_col] = df[age_col].fillna("Unrated").astype(str) # Fallback for empty strings

def typewriter_print(text, color_prefix="", delay=0.01):
    """Prints text character by character to create a typing animation effect."""
    sys.stdout.write(color_prefix)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def print_card(title, genre, age_rating, plot, mode_label):
    """Displays the movie card configuration utilizing the typing effect."""
    print("\n" + "=" * 60)
    typewriter_print(f"🎬 SELECTION STATUS: [{mode_label}]", Fore.CYAN)
    typewriter_print(f"📌 Title: {title}", Fore.YELLOW + Style.BRIGHT)
    typewriter_print(f"🔞 Age Rating: {age_rating}", Fore.RED + Style.BRIGHT)
    typewriter_print(f"🎭 Genre: {genre}", Fore.MAGENTA)
    
    # Label prints immediately, plot description gets animated typing layout
    sys.stdout.write(f"{Fore.GREEN}📖 Plot: {Style.DIM}")
    sys.stdout.flush()
    typewriter_print(plot, delay=0.008)
    print("=" * 60 + "\n")

# --- Continuous Main Interaction Loop ---
while True:
    print(f"{Fore.GREEN}{Style.BRIGHT}=== IMDB MOVIE LOOKUP SYSTEM ===")
    print("1. Pure Random Pick")
    print("2. Smart Keyword Match Pick")
    print("3. Exit Program")
    
    user_choice = input("\nEnter selection option (1, 2, or 3): ").strip()
    
    if user_choice == '1':
        row = df.sample(n=1).iloc[0]
        print_card(row[title_col], row[genre_col], row[age_col], row[overview_col], "RANDOM")
        
    elif user_choice == '2':
        prompt = input("\nWhat kind of plot or subject are you looking for?: ").strip().lower()
        if not prompt:
            print(f"{Fore.RED}Blank prompt entered. Returning to menu.\n")
            continue
            
        # Split keywords and aggregate total matches using native pandas lambda mapping
        keywords = prompt.split()
        match_counts = df[overview_col].str.lower().apply(lambda text: sum(1 for word in keywords if word in text))
        
        if match_counts.max() == 0:
            print(f"\n{Fore.RED}⚠️ Zero word matches found inside database overviews. Picking an automated fallback...")
            row = df.sample(n=1).iloc[0]
            print_card(row[title_col], row[genre_col], row[age_col], row[overview_col], "FALLBACK RANDOM")
        else:
            best_matches = df[match_counts == match_counts.max()]
            row = best_matches.sample(n=1).iloc[0]
            print_card(row[title_col], row[genre_col], row[age_col], row[overview_col], "SMART MATCH")
            
    elif user_choice == '3':
        print(f"\n{Fore.CYAN}Goodbye! Enjoy your movie night! 🍿")
        break
    else:
        print(f"{Fore.RED}Invalid option chosen. Please enter 1, 2, or 3.\n")
