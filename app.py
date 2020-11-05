#!/bin/python3
#-*-coding: utf-8-*-
import os


if os.system("cat input.txt >> data/dico.txt") == 0:
    os.system("rm input.txt; touch input.txt")
    print("New words processed\n")
    print("Cleaning...")
    if os.system("python3 scripts/sanitizer.py data/dico.txt > data/dico_f.txt") == 0:
        print("Cleaning complete\n")
        print("Now sorting... please wait...")
        #sorting and foramating
        if os.system("python3 scripts/main.py data/dico_f.txt output") == 0:
            print("Operation complete\n")
        else:
            print("Failed sorting")

    else:
        print("Failed cleaning!")
else:
    print("Failed adding the new words")