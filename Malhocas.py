#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, Setember 2020.
# --------------------------------------------------
import random
import time
import readchar
from colorama import Fore, Style

# argumentos de entrada, a alterar
tempo_max = 5
teclas_max = 0
letters = "abcdefghijklmnopqrstuvwxyz"

def modo_tempo():
    seconds = time.time()
    tempo_atual = time.localtime(seconds)
    tempo_inicio = time.mktime(tempo_atual)
    tempo_final=0

    while tempo_final - tempo_inicio < tempo_max:
        letra = random.choice(letters)
        seconds = time.time()
        tempo_atual = time.localtime(seconds)
        tempo_final = time.mktime(tempo_atual)

        print("Type the letter " + Fore.YELLOW + str(letra) + Style.RESET_ALL)
        pressed_key = readchar.readkey()

        if pressed_key == letra:
            print("You pressed " + Fore.GREEN + pressed_key + Style.RESET_ALL)
        else:
            print("You pressed " + Fore.RED + pressed_key + Style.RESET_ALL)


def modo_teclas():
    count = 0
    while count <teclas_max:
        letra=random.choice(letters)
        print("Type the letter " +  Fore.YELLOW + str(letra) + Style.RESET_ALL)
        pressed_key = readchar.readkey()
        if pressed_key == letra:
            print("You pressed " + Fore.GREEN + pressed_key + Style.RESET_ALL)
        else:
            print("You pressed " + Fore.RED + pressed_key + Style.RESET_ALL)
        count +=1





def main():
    print("Typing test PSR. Press any key to continue")
    pressed_continue=readchar.readkey()
    if pressed_continue:
        if teclas_max:
            modo_teclas()
        if tempo_max:
            modo_tempo()







if __name__ == "__main__":
    main()