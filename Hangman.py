#!/usr/bin/python3
""" Hangman game made by Facundo Diaz and Andres Rodriguez """
import os
import random
import time

""" COLOR VARIABLES """
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[32m'

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

# this function prints score table and name of player
def print_label(name, vidas):
    print(CGREEN + "PLAYER:", name, "AVAILABLES TRIES:", vidas, CEND)

# this function chose the word
def new_palabra():
    word_list = ["car", "dog", "doll", "cat", "cellphone", "computer", "mouse", "house", "doctor", "kitchen",  "jumper",  "soccer",
                 "skill", "deparment", "scene", "wood", "awareness", "foundation", "disease", "classroom", "opinion", "sister", "ball",]
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

# this function prints de message when the player lost the game
def defeat():
    os.system('clear')
    print_boneco(v1, v2, v3, v4, v5, v6, v7)
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
    print_boneco(v1, v2, v3, v4, v5, v6, v7)
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

# welcome message
print("Welcome to Hangman game")
print()
time.sleep(1)
print("Enter your name")

#declaration all variables
"""

m: is the number of deaths
b: is the flag to end the game
e: is the flag to print a error message
vx: is the position of draw
palabra: is the word of the game
arr: is a copy of palabra, this variable change when the player guess a letter
perdidas: this array contains the letters out of game

"""
name = input()
m = 0
b = 0
e = 0
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
        print("\n\n WRONG LETTERS")
        print("  |   |   |")
        print("  V   V   V")
        print_arr(perdidas)
    if e == 1:
        print(CRED + "\nPlease, guess a single letter or the whole word\n" + CEND)
        e = 0
    if e2 == 1:
        print(CRED + "\nPlease, guess an unused letter\n" + CEND)
        e2 = 0
    letra_elegida = input()
    if letra_elegida == palabra:
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
                    if m == 3:
                        v3 = chr(92)
                    if m == 4:
                        v4 = "|"
                    if m == 5:
                        v5 = "/"
                    if m == 6:
                        v6 = chr(92)
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
            e = 1