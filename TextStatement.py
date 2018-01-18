'''
Created on Jan 18, 2018

@author: hoymm
'''
from Timing import Timing


class TextStatement:
    def __init__(self, stringStatementToProcess):
        self.extractIdTimingAndTextDataFromString(stringStatementToProcess)

    def extractIdTimingAndTextDataFromString(self, txt):
        singleLines = txt.split('\n')
        if len(singleLines) > 1:
            self.Id = singleLines[0]
            self.Timing = Timing(singleLines[1])
            self.textToShow = singleLines[2:]

    def printInfo(self):
        print('ID: ' + str(self.Id) + '\nFROM ' + str(self.Timing.msFrom) + ' TO ' + str(self.Timing.msTo))
        for i in range(len(self.textToShow)):
            print(self.textToShow[i])
