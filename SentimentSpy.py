import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f'{Fore.CYAN} Welcome to Sentiment Spy {Style.RESET_ALL}')
user_name=input(f'{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}').strip()
if not user_name:
    user_name='Anonymous'
conversation_history=[]
print(f'\n{Fore.CYAN} Hello, agent {user_name}!')
print(f'type a sentence and I will analyze your sentences with textblob and show you the sentiment.')
print(f'Type{Fore.YELLOW} reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN},{Fore.YELLOW} exit, {Fore.CYAN}To quit.{Style.RESET_ALL}\n')
