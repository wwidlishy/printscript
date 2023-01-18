from sys import *
import sys
import logging

class v:
    filec = None

def parse(filecontents):
    v.filec = filecontents.replace("  ", "")
    v.filec = v.filec.replace(" ", "")
    v.filec = v.filec.replace("\n", "")
    v.filec = v.filec.replace("#nl", "\n")
    v.filec = v.filec.replace("#tab", "  ")
    v.filec = v.filec.replace("#s", " ")
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
