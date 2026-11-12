## les imports inter-package sont calculés depuis le package (la racine ou .venv si installé via pip)
# from text_analyser.text_cleaner import Cleaner
## ou à la rigueur avec un pseudo chemin relatif
from .text_cleaner import Cleaner

class Counter:
    ### version aggrégation <=> injection de dép.
    def __init__(self, cleaner: Cleaner):
        self.__text = cleaner.clean()

    ### version composition <=> couplage fort
    # def __init__(self, text: str):
    #     self.__text = Cleaner(text).clean()