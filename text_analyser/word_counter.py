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

    def get_occurences(self) -> dict:
        """
        1. alimenter un dico à partir de self.__text pour en faire un dictionnaire d'occurence 
           {"motA": x, "motB": y, ....}
           algo: en parcourant le texte, on regarde si un mot a déjà été ajouté dans le dico
              => +1
              sinon je le créé dans le dico
        2. comment je peux trier un dictionnaire ?
        """
        dico = {}
        for word in self.__text.split():
            if word in dico:
                dico[word] += 1
            else:
                dico[word] = 1

        return dict(sorted(
            dico.items(), 
            key=lambda tup: tup[1], 
            reverse=True
        )[:5])