#!/bin/python3
#-*-coding: utf-8-*-
import sys
import sort, dicformat


def main():
    """
    Usage | python main.py filename.txt output_file
          or
          | ./main.py filename.txt output_file
    """
    if len(sys.argv) < 3:
        print("File name missing")

    elif not (sys.argv[1].endswith(".txt")):
        print("Invalid file: Must be txt")

    else:
        filename = sys.argv[1]
        output_file = sys.argv[2]

        # Sorting
        lines = sort.wo_sort(filename)
        
        # Isolating and Formating...
        dico = dicformat.format_words(output_file, lines)


if __name__ == "__main__":
    main()