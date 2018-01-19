'''
Created on Jan 18, 2018

@author: hoymm
'''
from TextStatement import TextStatement


class Subtitles:
    def __init__(self, subtitlesFileName):
        self.subtitlesStatements = self.openFileAndConvertToSubtitlesStatements(subtitlesFileName)

    def openFileAndConvertToSubtitlesStatements(self, subtitlesFileName):
        subtitlesFilePath = 'Napisy/' + subtitlesFileName
        resultStatements = []
        try:
            self.subtitlesFile = open(subtitlesFilePath, 'r+w')
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:  # handle other exceptions such as attribute errors
            print "Unexpected error while trying to open file: " + subtitlesFilePath

        statemtentsList = self.subtitlesFile.read().split('\n\n')[0:-1]
        for i in range(len(statemtentsList)):
            textStatement = TextStatement(statemtentsList[i])
            resultStatements.append(textStatement)
        return resultStatements

    def _del_(self):
        try:
            self.subtitlesFile.close()
        except IOError:
            "Unable to close the file."
            raise
