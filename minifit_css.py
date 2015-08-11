#!/usr/bin/python
# removendo o minifit_file.py
import sys


sys.argv.pop(0)
nLine = ""
copy =[0, True]
final = ""
for param in sys.argv:
    # open file .CSS
    arquivo = open(param)

    # read file and remove \n (breaklins)
    linha = True
    while linha:
        linha = arquivo.readline()
        listaLinha = linha.split('\n')
        nLine += "".join(listaLinha)

    # remove Coments in CSS and spaces
    for c in range(1, len(nLine)):
        if nLine[c - 1] == "/" and nLine[c] == "*":
            copy[0] += 1
            copy[1] = False

        if nLine[c - 1] == "*" and nLine[c] == "/":
            copy[0] -= 1
            copy[1] = True

        if nLine[c] != ' ' and nLine[c] != '/' and copy == [0, True]:
            final += nLine[c]

    # I took the file name without the extension and added at the end of the file name ".min.css"
    name = param.split('.css')[0] + ".min.css"
    finalFile = open(name, 'w')
    finalFile.write(final)
    finalFile.close()