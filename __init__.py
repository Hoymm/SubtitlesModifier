#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SubtitlesProcessFiles.Subtitles import Subtitles
from Menu.MenuSaveFile import MenuSaveFile
from Menu.Menu import Menu

subtitlesModifier = Subtitles('napisy.srt')
menu = Menu(subtitlesModifier)
if menu.invokeMainMenu():
    menuSaveFile = MenuSaveFile(subtitlesModifier)
else:
    print("User did not make any changes.")

