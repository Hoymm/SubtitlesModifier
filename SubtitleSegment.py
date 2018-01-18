'''
Created on Jan 18, 2018

@author: hoymm
'''
class SubtitleSegment:
    elementID = 1
    msFrom = 0
    msTo = 0
    textToShow = '#'
    
    def __init__(self, textDataToProcess):
        print(textDataToProcess)