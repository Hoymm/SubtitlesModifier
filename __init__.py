#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Subtitles import Subtitles


def showMenu():
    print("MENU")
    print("1.Przesun napisy")
    print("2.Zmień prędkość wyświetlania")
    print("0.Wyjdź")
    choose = input('\nWybierz: ')

    if choose == 1:
        print("Przesuwam napisy")
    elif choose == 2:
        print("Zmieniam prędkość wyświetlania")
    elif choose == 0:
        print("Wychodzę z programu")
    else:
        print("Nieprawidłowa wartość")


subtitlesModifier = Subtitles('napisy.srt')
showMenu()

