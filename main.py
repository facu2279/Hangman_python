#!/usr/bin/python3
""" Hangman game made by Facundo Diaz and Andres Rodriguez """
import os
import random

os.system('clear')
def print_boneco(v1, v2, v3, v4, v5, v6, v7):
    print("     ____")
    print("    |    |")
    print("    |   "+v7+v1+v7)
    print("    |   "+v2+v4+v3)
    print("    |    "+v4)
    print("    |   "+v5,v6)
    print("____|____")

def print_label(name, vidas):
    print("PLAYER:", name, "AVAILABLES TRIES:", vidas)

def new_palabra():
    word_list = ["car", "dog", "doll", "cat", "cellphone", "computer", "mouse", "house", "doctor", "kitchen",  "jumper",  "soccer",
                 "skill", "deparment", "scene", "wood", "awareness", "foundation", "disease", "classroom", "opinion", "sister", "ball",]
    word = random.choice(word_list)
    return(word)
def chequear_existencia(letra_elegida, arr, palabra):
    for i in range(0,len(palabra)):
        if letra_elegida == palabra[i]:
            arr[i] = letra_elegida
    return arr
def check_win(arr, palabra):
    for i in range(0,len(palabra)):
        if arr[i] == palabra[i]:
            continue
        else:
            return 0
    return 1
def print_arr(arr):
    for i in range(0, len(arr)):
        print(arr[i] + " ", end="")
    print()

print("Enter your name")
name = input()
m = 0
b = 0
v1 = v2 = v3 = v4 = v5 = v6 = v7 = " "
palabra = new_palabra()
arr = []
perdidas = []
for i in range(0, len(palabra)):
    arr.append("_")


while(b != 1):
    os.system('clear')
    print_label(name, 7 - m)
    print_boneco(v1, v2, v3, v4, v5, v6, v7)
    print_arr(arr)
    if m != 0:
        print("\n\n LETTERS OUT OF GAME")
        print("  |   |   |")
        print("  V   V   V")
        print_arr(perdidas)
    letra_elegida = input()
    if letra_elegida == palabra:
        os.system('clear')
        print_boneco(v1, v2, v3, v4, v5, v6, v7)
        print("\n\n*************************")
        print("*************************")
        print("Congrats you won the game")
        print("-------------------------")
        print("The word was", palabra)
        print("*************************")
        print("*************************")
        b = 1
    elif len(letra_elegida) == len(palabra):
        v1 = "O"
        v2 = "/"
        v3 = chr(92)
        v4 = "|"
        v5 = "/"
        v6 = chr(92)
        v7 = "_"
        os.system('clear')
        print_boneco(v1, v2, v3, v4, v5, v6, v7)
        print("\n\n*****************")
        print("*****************")
        print("You lost the game")
        print("*****************")
        print("*****************")
        b = 1
    else:
        if len(letra_elegida) == 1 and (ord(letra_elegida) >= 97 and ord(letra_elegida) <= 122):
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
                    os.system('clear')
                    print_boneco(v1, v2, v3, v4, v5, v6, v7)
                    print("\n\n*****************")
                    print("*****************")
                    print("You lost the game")
                    print("*****************")
                    print("*****************")
                    b = 1
                else:
                    perdidas.append(letra_elegida)
            else:
                if check_win(arr, palabra):
                    os.system('clear')
                    print_boneco(v1, v2, v3, v4, v5, v6, v7)
                    print("\n\n*************************")
                    print("*************************")
                    print("Congrats you won the game")
                    print("-------------------------")
                    print("The word was", palabra)
                    print("*************************")
                    print("*************************")
                    b = 1
        else:
            print("error")
