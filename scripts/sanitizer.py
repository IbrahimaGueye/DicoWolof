#!/bin/python3
#-*- coding: utf-8 -*-
import sys

def main():
    words = []
    with open(sys.argv[1], "r") as file:
        words = file.readlines()
        words = list(dict.fromkeys(words))
    final_output = []
    for word in words:
        if word[0] == "•":
            final_output.append(word[1:])
        else:
            final_output.append(word)

    for word in final_output:
        print(word.strip())

if __name__ == "__main__":
    main()
