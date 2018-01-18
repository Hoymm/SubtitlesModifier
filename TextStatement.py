'''
Created on Jan 18, 2018

@author: hoymm
'''
import re
from TimeLineIntoDigits import TimeLineIntoDigits
class TextStatement:
    def __init__(self, statementToProcess):
        singleLines = statementToProcess.split('\n')
        if (len(singleLines) > 1):
            self.Id = singleLines[0]
            self.Timing = TimeLineIntoDigits(singleLines[1])
            self.textToShow = singleLines[2:]
        
    def printInfo(self):
        print('ID: ' + str(self.Id) + '\nFROM ' + str(self.Timing.msFrom) + ' TO ' + str(self.Timing.msTo))
        for i in range(len(self.textToShow)):
            print(self.textToShow[i])

            
            
            
            
            