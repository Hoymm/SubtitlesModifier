'''
Created on Jan 18, 2018

@author: hoymm
'''
import re


class WrongTimeFormat(Exception):
    def __init__(self,*args):
        Exception.__init__(self, *args)

class Timing:
    def __init__(self, stringLine):
        try:
            self.convertStringTimingLineIntoFromToValues(stringLine)
        except AttributeError:
            print("TimeLineIntoDigits was unable to cast String format of timing into integer one")
            raise

    def convertStringTimingLineIntoFromToValues(self, stringLine):
        fromAndToMilliseconds = re.findall('\d{2}:\d{2}:\d{2},\d{3}', stringLine)
        try:
            self.msFrom = Timing.timeStringLineIntoMilliseconds(fromAndToMilliseconds[0])
            self.msTo = Timing.timeStringLineIntoMilliseconds(fromAndToMilliseconds[1])
        except WrongTimeFormat:
            print("Error when trying to convert string time format into integer (milliseconds)")

    # method converts string format i.e. 03:11:01;823 (hh:mm:ss;fff) into milliseconds
    @staticmethod
    def timeStringLineIntoMilliseconds(stringTime):
        strNumbs = re.findall('\d+', str(stringTime))

        if len(strNumbs) < 4:
            raise WrongTimeFormat("sdafd")

        hoursAsMs = int(strNumbs[0]) * 3600 * 1000
        minAsMs = int(strNumbs[1]) * 60 * 1000
        secondsAsMs = int(strNumbs[2]) * 1000
        ms = int(strNumbs[3])

        return int(hoursAsMs + minAsMs + secondsAsMs + ms)
