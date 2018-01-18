'''
Created on Jan 18, 2018

@author: hoymm
'''
from TextStatement import TextStatement
class Subtitles:
    def __init__(self, subtitlesFileName):
        try:
            self.subtitlesFile = open(subtitlesFileName,'r+w')
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except: #handle other exceptions such as attribute errors
            print "Unexpected error while trying to open file: " + subtitlesFileName
            
        statemtentsList = self.subtitlesFile.read().split('\n\n')[0:-1]
        processedStatements = []
        for i in range(len(statemtentsList)):
            processedStatements.append(TextStatement(statemtentsList[i]))
        processedStatements[5].printInfo()
     
        
    def _del_(self):
        try:
            self.subtitlesFile.close()
        except:
            "Unable to close the file."