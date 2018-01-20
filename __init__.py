#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SubtitlesProcessFiles.Subtitles import Subtitles
from Menu.Menu import Menu

subtitlesModifier = Subtitles('napisy.srt')
menu = Menu(subtitlesModifier)
if menu.invokeMainMenu():
    newFileName = raw_input('Podaj nazwę pliku do zapisania: ')
    subtitlesModifier.saveToFile(newFileName)

else:
    print("User did not make any changes.")

