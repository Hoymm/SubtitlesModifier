#!/usr/bin/env python
# -*- coding: utf-8 -*
from MenuMoveSubtitles import MenuMoveSubtitles
from MenuChangeFPS import MenuChangeFPS
class Menu:
    def __init__(self, subtitles):
        self.subtitles = subtitles
        self.menuMoveSubtitles = MenuMoveSubtitles(subtitles)
        self.menuChangeFPS = MenuChangeFPS(subtitles)

    def invokeMainMenu(self):
        choose = '-1'
        while choose != '1' and choose != '2' and choose != '0':
            print("\nMENU")
            print("1.Przesun napisy")
            print("2.Zmień prędkość wyświetlania")
            print("0.Wyjdź")
            choose = raw_input('Wybierz: ')

            if choose == '1':
                if self.menuMoveSubtitles.invoke():
                    print("Przesunięcie napisów zakończone sukcesem.")
                    return True
            elif choose == '2':
                print("Zmieniam prędkość wyświetlania")
            elif choose == '0':
                print("Wychodzę z programu")
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie.")
                raw_input("Wciśnij enter by kontynuować...")