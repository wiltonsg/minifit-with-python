#!/usr/bin/python
import sys
import os


class Minifit():

    def __init__(self, argv):
        super(Minifit, self).__init__()
        self.dir = os.path.dirname(os.path.abspath(__file__))
        for param in argv:

            if argv[0].split('.')[-1].lower() == 'css':
                self.min_css(param)

            if argv[0].split('.')[-1].lower() == 'js':
                self.min_js(param)

    def min_css(self, param):
        nLine = ""
        copy =[0, True]
        final = ""

        try:
            # open file .CSS
            arquivo = open(param)
        except Exception:
            print("I did not find the file(s) css / js.\nCheck if the files are in this folder: "+ self.dir)
            exit()

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

    def min_js(self, param):
        nLine = ""
        copy =[0, True]
        final = ""
        last = False

        try:
            # open file .JS
            arquivo = open(param)
        except Exception:
            print("I did not find the file(s) css / js.\nCheck if the files are in this folder: "+ self.dir)
            exit()

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


if __name__ == "__main__":
    sys.argv.pop(0)
    miniFit = Minifit(sys.argv)