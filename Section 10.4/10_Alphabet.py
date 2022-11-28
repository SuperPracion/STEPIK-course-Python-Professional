class Alphabet:
    LANG = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}

    def __init__(self, language):
        self.language = language
        self.letters = iter(self.LANG[language])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.letters)
        except:
            self.letters = iter(self.LANG[self.language])
            return next(self.letters)


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
