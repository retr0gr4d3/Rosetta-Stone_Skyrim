from os import system, name
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def invalidAnswer():
    clear()
    print("Skyrim Dragon Translation v0.1\nOops! I don't think that was right.\nCheck your spelling and try again.")
    time.sleep(2)
    clear()

def main():
    while True:
        dov = input("Skyrim Dragon Translation v0.1\nThis tool requires the user to input dragon words, in order to translate them to English.\nPlease enter a word to translate: ").lower()
        if dov == "aan" :
            clear()
            print("Skyrim Dragon Translation V0.1\n'Aan' (dov) translates to 'A' (eng)")
            break
        elif dov == "suleyk" :
            clear()
            print("Skyrim Dragon Translation v0.1\n'Suleyk' (dov) translates to 'Ability' (eng)")
            break
        else:
            invalidAnswer()
main()
