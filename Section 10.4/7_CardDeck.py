class CardDeck:
    DECK = [str(i) + ' ' + j
            for j in ['пик', 'треф', 'бубен', 'червей']
            for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']]

    def __init__(self):
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.DECK[self.index]
        except:
            raise StopIteration

cards = CardDeck()

print(next(cards))
print(next(cards))