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

    def moveTimeByMs(self, ms):
        self.Timing.msTo += ms
        self.Timing.msFrom += ms

    def getSRTFormat(self):
        result = str(self.Id) + "\n" + self.msToStringFormat(self.Timing.msFrom) + " --> " + self.msToStringFormat(self.Timing.msTo) + "\n"
        for i in range(len(self.textToShow)):
            result += self.textToShow[i] + '\n'
        return result + "\n"

    def msToStringFormat(self, ms):
        negative = ms < 0
        if negative:
            ms *= -1

        msValue = ms - (ms/1000*1000)
        msStr = "%03d" % (msValue,)
        sec = ms/1000

        secValue = sec - (sec/60*60)
        secStr = "%02d" % (secValue,)
        min = sec/60

        minValue = min - (min/60*60)
        minStr = "%02d" % (minValue,)
        hour = min/60

        hoursValue = hour - (hour/60*60)
        hoursStr = "%02d" % (hoursValue,)

        result = hoursStr + ":" + minStr + ":" + secStr + "," + msStr
        if negative:
            result = "-" + result
        return result


