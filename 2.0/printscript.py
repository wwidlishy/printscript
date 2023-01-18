from sys import *
import sys
from termcolor import colored
from colorama import just_fix_windows_console

just_fix_windows_console()

class v:
    filec = None

def parse(filecontents):
    v.filec = filecontents.replace("  ", "")
    v.filec = v.filec.replace(" ", "")
    v.filec = v.filec.replace("\n", "")
    v.filec = v.filec.replace("#nl", "\n")
    v.filec = v.filec.replace("#tab", "  ")
    v.filec = v.filec.replace("#s", " ")
    while True:
        colors = ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta','white', 'light_grey', 'dark_grey', 'black', 'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_cyan', 'light_magenta']
        atrs = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']
        formats = []
        for i in colors:
            if (f"??{i}??" and "(" and ")") in v.filec:
                text = v.filec[v.filec.index("(")+1:v.filec.index(")")]
                v.filec = v.filec.replace(f"??{i}??({text})", colored(text, i))
        for i in atrs:
            if (f"??{i}??" and "(" and ")") in v.filec:
                text = v.filec[v.filec.index("(")+1:v.filec.index(")")]
                v.filec = v.filec.replace(f"??{i}??({text})", colored(text, attrs=[i]))
        if ("??color_list??") in v.filec:
            for j in colors:
                formats.append(f"    {colors.index(j)}) " + colored(f"??{colors[colors.index(j)]}??", colors[colors.index(j)]) + "\n")
            for j in atrs:
                formats.append(f"    {atrs.index(j)}) " + colored(f"??{atrs[atrs.index(j)]}??", attrs = [j]) + "\n")
            colorlist = f"PrintScript Format List:"
            v.filec = v.filec.replace("??color_list??", "")
            print(colorlist)
            for k in formats:
                print(k, end='')
        break
    print(v.filec, end='')
    v.filec != None
def open_file(filename):
    data = open(filename, 'r').read()
    return data

x = 0

def run():
    data = open_file(argv[1])
    do = parse(data)

run()