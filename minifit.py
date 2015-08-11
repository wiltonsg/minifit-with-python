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

    # open file .CSS or .JS
    def openFile(self, filename):
        try:
            arquivo = open(filename)
            return(arquivo)
        except Exception:
            print("I did not find the file(s) css / js.\nCheck if the files are in this folder: "+ self.dir)
            exit()

    # read file and remove Coments Line
    def removeLinesComent(self, arquivo):
        lines = True
        nLine = ""
        while lines:
            lines = arquivo.readline()
            for x in range(0, len(lines)):
                if lines[x] == '/' and lines[x + 1] == '/':
                    break
                else:
                    nLine += lines[x]
        return(nLine)

    # remove Block Coments and Line Feed and ' '
    def removeBlockComent(self, nLine):
        copy =[0, True]
        last = False
        Nremove = False
        final = ""

        for c in range(0, len(nLine) - 1):
            if nLine[c] == '/' and nLine[c + 1] == '*':
                copy[0] += 1
                copy[1] = False

            if nLine[c - 1] == '*' and nLine[c] == '/':
                copy[0] -= 1
                copy[1] = True
                last = True

            if nLine[c] == '@':
                Nremove = True

            if nLine[c] == ' ':
                if nLine[c-3] == 'v' and nLine[c-2] == 'a' and nLine[c-1] == 'r' or Nremove:
                    Nremove = False
                else:
                    last = True

            if copy == [0, True] and nLine[c] != '\n':
                if last:
                    last = False
                else:
                    final += nLine[c]
        return(final)

    # save file name.min.css or name.min.js
    def saveFileMin(self, nLine, param):
        if param.split('.')[-1:][0].lower() == 'js':
            name = '.'.join(param.split('.')[:-1]) + ".min.js"
        elif param.split('.')[-1:][0].lower() == 'css':
            name = '.'.join(param.split('.')[:-1]) + ".min.css"
        
        finalFile = open(name, 'w')
        finalFile.write(nLine)
        finalFile.close()

    def min_js(self, param):
        arquivo = self.openFile(param)
        nLine = self.removeLinesComent(arquivo)
        nLine = self.removeBlockComent(nLine)

        self.saveFileMin(nLine, param)

    def min_css(self, param):
        arquivo = self.openFile(param)
        nLine = arquivo.read()
        nLine = self.removeBlockComent(nLine)

        self.saveFileMin(nLine, param)


if __name__ == "__main__":
    sys.argv.pop(0)
    miniFit = Minifit(sys.argv)