# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
╭━━╮╱╱╱╱╱╭╮╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
╰┫┣╯╱╱╱╱╭╯╰╮╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╭╯╰╮
╱┃┃╭━╮╭━┻╮╭╋━━┫╰━╯┣━━┳━━┳━━┳┻╮╭╋━━┳━╮
╱┃┃┃╭╮┫━━┫┃┃╭╮┃╭╮╭┫┃━┫╭╮┃╭╮┃╭┫┃┃┃━┫╭╯
╭┫┣┫┃┃┣━━┃╰┫╭╮┃┃┃╰┫┃━┫╰╯┃╰╯┃┃┃╰┫┃━┫┃
╰━━┻╯╰┻━━┻━┻╯╰┻╯╰━┻━━┫╭━┻━━┻╯╰━┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯"""

urls = [
    "Made By Pratyush Sharma"
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Producer: Pratyush Sharma"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Follow me On Instagram @Pratyush.sharma2710")

    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
