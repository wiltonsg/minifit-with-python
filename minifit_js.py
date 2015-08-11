#!/usr/bin/python
import sys


sys.argv.pop(0)
nLine = ""
copy =[0, True]
final = ""
last = False
for param in sys.argv:
    # open file .JS
    arquivo = open(param)

    # read file and remove \n (breaklins) and Coments Line
    lines = True
    while lines:
        lines = arquivo.readline()
        for x in range(0, len(lines)):
            if lines[x] == '/' and lines[x + 1] == '/':
                break
            else:
                nLine += lines[x]


    # remove Block Coments in JS and spaces
    for c in range(0, len(nLine)):
        if nLine[c] == "/" and nLine[c+1] == "*":
            copy[0] += 1
            copy[1] = False

        if nLine[c - 1] == "*" and nLine[c] == "/":
            copy[0] -= 1
            copy[1] = True
            last = True

        if nLine[c] != ' ' and copy == [0, True] and nLine[c] != '\t' and nLine[c] != '\n':
            if last:
                last = False
            else:
                final += nLine[c]

    # I took the file name without the extension and added at the end of the file name ".min.js"
    name = param.split('.js')[0] + ".min.js"
    finalFile = open(name, 'w')
    finalFile.write(final)
    finalFile.close()