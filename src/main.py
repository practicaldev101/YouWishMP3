from libs.downloader import Audio
from colorama import Fore
from os import system, name

def logo() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("""
__   __          _    _ _     _    ___  _________ _____ 
\ \ / /         | |  | (_)   | |   |  \/  || ___ \____ |
 \ V /___  _   _| |  | |_ ___| |__ | .  . || |_/ /   / /
  \ // _ \| | | | |/\| | / __| '_ \| |\/| ||  __/    \ \\
  | | (_) | |_| \  /\  / \__ \ | | | |  | || |   .___/ /
  \_/\___/ \__,_|\/  \/|_|___/_| |_\_|  |_/\_|   \____/                                                         
    
    By Practical Programmer | GitHub:practicaldev101
""")

def main() -> None:
    try:
        logo()
        filename = "music.txt"
        with open(filename, "r") as file:
            for url in file.readlines():
                if url.strip() != "":
                    Audio(url).downloadAudio()
            file.close()
        print(Fore.GREEN + "[ + ] File " + filename + " finished." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.YELLOW + "[ ! ] File " + filename + " not found, creating new one" + Fore.RESET)
        with open(filename, "w") as file: file.close()
        print(Fore.YELLOW + "[ ! ] Please, fill the file and try again" + Fore.RESET)
    input("Press ENTER to exit...")

if __name__ == "__main__":
    main()