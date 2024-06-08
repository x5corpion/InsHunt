# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
  
██ ███    ██ ███████ ██   ██ ██    ██ ███    ██ ████████ 
██ ████   ██ ██      ██   ██ ██    ██ ████   ██    ██    
██ ██ ██  ██ ███████ ███████ ██    ██ ██ ██  ██    ██    
██ ██  ██ ██      ██ ██   ██ ██    ██ ██  ██ ██    ██    
██ ██   ████ ███████ ██   ██  ██████  ██   ████    ██    

"""

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Producer: Hichigo THT, Translator: x_5corpion"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> I would like to thank https://github.com/tarik0/instaspamv4 for the repo")
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
