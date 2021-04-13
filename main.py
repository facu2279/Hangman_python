#!/usr/bin/python3
""" Hangman game made by Facundo Diaz and Andres Rodriguez """
import os

def print_boneco(v1, v2, v3, v4, v5, v6, v7):
    print("     ____")
    print("    |    |")
    print("    |   "+v7+v1+v7)
    print("    |   "+v2+v4+v3)
    print("    |    "+v4)
    print("    |   "+v5,v6)
    print("____|____")

print("Inserte su nombre")
name = input()
print("Player:", name)

v1 = v2 = v3 = v4 = v5 = v6 = v7 = " "
print_boneco(v1, v2, v3, v4, v5, v6, v7)

palabra = "computadora"

print("")

for i in range(0, len(palabra)):
    print("_ ", end="")
print()

"""os.system('clear')"""
v1 = "O"
v2 = "/"
v3 = chr(92)
v4 = "|"
v5 = "/"
v6 = chr(92)
v7 = "_"

print_boneco(v1, v2, v3, v4, v5, v6, v7)

