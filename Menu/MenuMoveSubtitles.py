#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SubtitlesProcessFiles.Timing import Timing
from SubtitlesProcessFiles.Timing import WrongTimeFormat
from enum import Enum


class Direction(Enum):
    BACKWARD = 1
    FORWARD = 2
    EXIT = 0

class MenuMoveSubtitles:
    def __init__(self, subtitles):
        self.subtitles = subtitles

    def invoke(self):
        direction = self.getDirection()
        if direction != Direction.EXIT:
            self.timeToMove = self.getAndCalculateTimeToMove(direction)
            for i in range(len(self.subtitles.subtitlesStatements)):
                self.subtitles.subtitlesStatements[i].moveTimeByMs(self.timeToMove)
            return True
        return False

    def getAndCalculateTimeToMove(self, direction):
        timeToMove = self.getTimeToMoveSubtitles()
        if direction == Direction.BACKWARD:
            timeToMove *= -1
        return timeToMove

    def getDirection(self):
        choose = '-1'
        while choose != '1' and choose != '2' and choose != '0':
            print("\nPodaj kierunek przesunięcia napisów:")
            print("1. Do tyłu")
            print("2. Do przodu")
            print("0. Wyjdź")

            choose = raw_input('Wybór: ')
            if choose == '1':
                print("Wybrałeś przesuwanie napisów do tyłu")
                return Direction.BACKWARD
            elif choose == '2':
                print("Wybrałeś przesuwanie napisów do przodu")
                return Direction.FORWARD
            elif choose == '0':
                return Direction.EXIT
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie.")
                raw_input("Wciśnij enter by kontynuować...")

    @staticmethod
    def getTimeToMoveSubtitles():
        try:
            print("\nWybierz czas o jaki chcesz przesunąć napisy")
            print("musisz użyć formatu hh:mm:ss;fff")
            print("np. \"01:32:04;23\" oznacza przesunięcie o 1 godzine, 32 minuty 4 sekundy i 232 milisekundy")
            subtitlesTimeChange = raw_input('Podaj czas przesunięcia w odpowiednim formacie: ')
            msToMove = Timing.timeStringLineIntoMilliseconds(subtitlesTimeChange)
            return msToMove
        except WrongTimeFormat:
            print("Błędny format podanych danych, spróbuj ponownie.")
            print("Pamiętaj że ilość cyfr musi zgadzać się z formatem")
            raw_input("Wciśnij enter by kontynuować...")
            MenuMoveSubtitles.getTimeToMoveSubtitles()