'''
Created on Jan 18, 2018

@author: hoymm
'''
import re
import sys
class TimeLineIntoDigits:
    def __init__(self, stringLine):
        try:
            self.convertStringTimingLineIntoTwoIntegerValues(stringLine)
        except AttributeError:  
            print("TimeLineIntoDigits was unable to cast String format of timing into integer one")
            raise
        
    def convertStringTimingLineIntoTwoIntegerValues(self, stringLine):
            fromAndToMilliseconds = re.findall('\d{2}:\d{2}:\d{2},\d{3}', stringLine)
            self.msFrom = self.timeStringLineIntoMilliseconds(fromAndToMilliseconds[0])
            self.msTo = self.timeStringLineIntoMilliseconds(fromAndToMilliseconds[1])
    
    
    # method converts string format i.e. 03:11:01;823 (hh:mm:ss;fff) into milliseconds      
    def timeStringLineIntoMilliseconds(self, stringTime):
        strNumbs = re.findall('\d+', stringTime)
        
        hoursAsMs = int(strNumbs[0])*3600*1000
        minAsMs = int(strNumbs[1])*60*1000
        secondsAsMs = int(strNumbs[2])*1000
        ms = int(strNumbs[3])
        
        return hoursAsMs+minAsMs+secondsAsMs+ms