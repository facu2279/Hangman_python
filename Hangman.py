#!/usr/bin/python3
""" Hangman game made by Facundo Diaz and Andres Rodriguez """
import os
import random
import time

""" COLOR VARIABLES """
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[32m'
CYELLOW = '\033[33m'
CCYAN = '\033[36m'
CVAR = CGREEN

# Clean screen before start the game
os.system('clear')

# this function prints the man
def print_boneco(v1, v2, v3, v4, v5, v6, v7):
    print("     ____")
    print("    |    |")
    print("    |   "+v7+v1+v7)
    print("    |   "+v2+v4+v3)
    print("    |    "+v4)
    print("    |   "+v5,v6)
    print("____|____")

# this function prints the man
def print_boneco_red(v1, v2, v3, v4, v5, v6, v7):
    print(CRED + "     ____")
    print("    |    |")
    print("    |   "+v7+v1+v7)
    print("    |   "+v2+v4+v3)
    print("    |    "+v4)
    print("    |   "+v5,v6)
    print("____|____" + CEND)

# this function prints the man
def print_boneco_green(v1, v2, v3, v4, v5, v6, v7):
    print(CGREEN + "     ____")
    print("    |    |")
    print("    |   "+v7+v1+v7)
    print("    |   "+v2+v4+v3)
    print("    |    "+v4)
    print("    |   "+v5,v6)
    print("____|____" + CEND)

# this function prints score table and name of player
def print_label(name, vidas):
    if name == "exit" or name == "quit":
        good_bye()
    if name == "":
        name = "Guest"
    cant_guiones = 38 + len(name)
    table = "-" * cant_guiones
    print(" " + table)
    print("|   " "PLAYER:"+ CYELLOW, name, CEND + CVAR + "    AVAILABLES TRIES:", vidas, "<3" + CEND, " |")
    print(" " + table)

# this function chose the word
def new_palabra():
    word_list = ["car", "dog", "doll", "cat", "cellphone", "computer", "mouse", "house", "doctor", "kitchen",  "jumper",  "soccer",
                 "skill", "deparment", "scene", "wood", "awareness", "foundation", "disease", "classroom", "opinion", "sister", "ball",
                 "rain", "book", "pencil", "robot", "coffe", "cupcake", "shirt", "charger", "unfortunate",
                 "dirty", "tail", "guess", "mother", "father", "paper", "bind", "rugby", "notice", "effect"]
    word = random.choice(word_list)
    return(word)

# this function checks if the letters match with word
def chequear_existencia(letra_elegida, arr, palabra):
    for i in range(0,len(palabra)):
        if letra_elegida == palabra[i]:
            arr[i] = letra_elegida
    return arr

# this function check if input word match with original word
def check_win(arr, palabra):
    for i in range(0,len(palabra)):
        if arr[i] == palabra[i]:
            continue
        else:
            return 0
    return 1

# This function prints array more beautifully
def print_arr(arr):
    print()
    for i in range(0, len(arr)):
        print(arr[i] + " ", end="")
    print()

def print_arr_v2(arr):
    table = "-" * 18
    print(CRED + table + CEND)
    for i in range(0, len(arr)):
        print(" " + arr[i] + " ", end="")
    print()
    print(CRED + table + CEND)

def good_bye():
    os.system('clear')
    print("\n\n ---------------\n|\t\t|\n|   Good Bye    |\n", end="")
    print("|               |\n", end="")
    print(" ---------------\n\n", end="")
    time.sleep(2)
    os.system('clear')
    exit()

# this function prints de message when the player lost the game
def defeat():
    os.system('clear')
    print_boneco_red(v1, v2, v3, v4, v5, v6, v7)
    print("\n\n*************************", end=time.sleep(0.6))
    print("*************************", end=time.sleep(0.6))
    print(CRED + "You " + CEND, end=time.sleep(0.6))
    print(CRED + "      lost " + CEND, end=time.sleep(0.6))
    print(CRED + "             the " + CEND, end=time.sleep(0.6))
    print(CRED + "                    game " + CEND, end=time.sleep(0.6))
    print("*************************", end=time.sleep(0.6))
    print(CRED + "** The word was", palabra, "**" + CEND, end=time.sleep(0.6))
    print("*************************", end=time.sleep(0.6))
    print("*************************", end=time.sleep(0.6))

# this function prints de message when the player won the game
def victory():
    os.system('clear')
    print_boneco_green(v1, v2, v3, v4, v5, v6, v7)
    print("\n\n***************************", end=time.sleep(0.6))
    print("***************************", end=time.sleep(0.6))
    print(CGREEN + "Congrats" + CEND, end=time.sleep(0.6))
    print(CGREEN + "         you" + CEND, end=time.sleep(0.6))
    print(CGREEN + "             won" + CEND, end=time.sleep(0.6))
    print(CGREEN + "                  the" + CEND, end=time.sleep(0.6))
    print(CGREEN + "                       game" + CEND, end=time.sleep(0.6))
    print("***************************", end=time.sleep(0.6))
    print(CGREEN + "** The word was", palabra, "**" + CEND, end=time.sleep(0.6))
    print("***************************", end=time.sleep(0.6))
    print("***************************", end=time.sleep(0.6))

def print_man():
    print("At the beginning of the game you have 7 tries.")
    print("\nTo play you simply have to insert a letter and press", end="")
    print("enter\nIf the letter is in the word you will see it.")
    print("\nIn case the letter is wrong an attempt will be discounted\nYou will ", end="")
    print("be able to see a section with letters that the word does ", end="")
    print("not have.\nIf you think you know the whole word, type it and ", end="")
    print("hit enter, but be careful!!!\nIf you don't guess the correct word, ", end="")
    print("you will lose the game instantly")
    print("To end the game, type quit or exit")
    print("\n\n\n\n\nThe manual will close automatically in a few seconds and the game will restart")
    print("\n\n\n\t\t\t\tHave fun!")
    print("\n\n\n\t\tMade by Facundo Diaz and Andres Rodriguez")

# welcome message
print("Welcome to Hangman game")
print()
time.sleep(1)
print("Enter your name")

#declaration all variables
"""

m: is the number of deaths
b: is the flag to end the game
ex: is the flag to print a error message
vx: is the position of draw
palabra: is the word of the game
arr: is a copy of palabra, this variable change when the player guess a letter
perdidas: this array contains the letters out of game

"""
name = input()
m = 0
b = 0
e1 = 0
e2 = 0
v1 = v2 = v3 = v4 = v5 = v6 = v7 = " "
palabra = new_palabra()
arr = []
perdidas = []

# give initial values to the player word
for i in range(0, len(palabra)):
    arr.append("_")

while(b != 1):
    os.system('clear')
    print_label(name, 7 - m)
    print_boneco(v1, v2, v3, v4, v5, v6, v7)
    print_arr(arr)
    if m != 0:
        print(CRED + "\n\n WRONG LETTERS" + CEND)
        print()
        print("  |   |   |")
        print("  V   V   V")
        print_arr_v2(perdidas)
    else:
        print("\nIf you need help, type help and enter")
    if e1 == 1:
        print(CRED + "\nPlease, guess a single letter or the whole word\n" + CEND)
        e1 = 0
    if e2 == 1:
        print(CRED + "\nPlease, guess an unused letter\n" + CEND)
        e2 = 0
    print()
    letra_elegida = input()
    if letra_elegida == "help":
        os.system('clear')
        print_man()
        time.sleep(15)
    elif letra_elegida == "exit" or letra_elegida == "quit":
        good_bye()
        break
    elif letra_elegida == palabra:
        victory()
        b = 1
    elif len(letra_elegida) == len(palabra):
        v1 = "O"
        v2 = "/"
        v3 = chr(92)
        v4 = "|"
        v5 = "/"
        v6 = chr(92)
        v7 = "_"
        defeat()
        b = 1
    else:
        if len(letra_elegida) == 1 and (ord(letra_elegida) >= 97 and ord(letra_elegida) <= 122):
            if (letra_elegida not in perdidas) and (letra_elegida not in arr):
                prov = arr.copy()
                arr = chequear_existencia(letra_elegida, arr, palabra)
                if arr == prov:
                    m = m + 1
                    if m == 1:
                        v1 = "O"
                    if m == 2:
                        v2 = "/"
                        CVAR = CCYAN
                    if m == 3:
                        v3 = chr(92)
                    if m == 4:
                        v4 = "|"
                        CVAR = CYELLOW
                    if m == 5:
                        v5 = "/"
                    if m == 6:
                        v6 = chr(92)
                        CVAR = CRED
                    if (m == 7):
                        v7 = "_"
                        defeat()
                        b = 1
                    else:
                        perdidas.append(letra_elegida)
                else:
                    if check_win(arr, palabra):
                        victory()
                        b = 1
            else:
                e2 = 1
        else:
            e1 = 1