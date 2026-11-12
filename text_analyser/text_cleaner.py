from string import punctuation
import re


class Cleaner:
    def __init__(self, text: str):
        self.__text = text

    def __clean_punctuation(self) -> None:
        """
        met à jour l'attribut text en nettoyant la ponctuation
        """
        self.__text = re.sub(pattern=f"[{punctuation}]", repl=" ", string= self.__text)

    def __clean_crlf(self) -> None:
        # ----------------------> chaine "raw" qui exprime le \ en tant que caractère
        # self.__text = re.sub(pattern=r"\r?\n", repl=" ", string= self.__text)
        self.__text = " ".join(self.__text.splitlines())

    def __clean_spaces(self):
        self.__text = re.sub(pattern=f" +", repl=" ", string= self.__text)

    def __clean_little_words(self):
        self.__text =  " ".join(
            filter(
                lambda w: len(w) > 3, 
                self.__text.split()
            )
        )
        # words = []
        # for word in self.__text.split():
        #     if len(word) > 3:
        #         words.append(word)
        # self.__text = " ".join(words)


    def clean(self):
        self.__clean_punctuation()
        self.__clean_crlf()
        self.__clean_spaces()
        self.__clean_little_words()
        return self.__text.lower()

    @classmethod
    def nimp_statique_methode_dans_une_classe_concrete(cls, *args, **kwars):
        """
        méthode uniquement utilisable que par la classe !!!
        """
        pass


class StaticCleaner:
        """
        pas d'instanciation car pas d'état
        """
        @staticmethod
        def __clean_punctuation(text) -> str:
            return re.sub(pattern=f"[{punctuation}]", repl=" ", string=text)

        @staticmethod
        def clean(text: str) -> str:
            text = StaticCleaner.__clean_punctuation(text)
            # text = StaticCleaner.__clean_crlf(text)
            # text = StaticCleaner.__clean_spaces(text)
            # text = StaticCleaner.__clean_little_words(text)
            return text.lower()

