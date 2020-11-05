import icu

def wo_sort(filename):
    """
    Desc    | Sorts alphabeticaly (Wolof) the lines in the given file
    param   | filename: Name of the file
    returns | A list with all the lines, sorted
    """
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    collator = icu.Collator.createInstance(icu.Locale('wo_SN.UTF-8'))
    final_lines = list(dict.fromkeys(lines))
    final_lines.sort(key=collator.getSortKey)


    return final_lines

