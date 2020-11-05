#!/bin/python3
#-*- coding: utf-8 -*-
import sys

def main():
    words = []
    with open(sys.argv[1], "r") as file:
        words = file.readlines()

    words = list(dict.fromkeys(words))
    
    for word in words:
        print(word.strip())
    
if __name__ == "__main__":
    main()