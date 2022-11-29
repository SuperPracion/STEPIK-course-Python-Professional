def card_deck(suit_ignore):
    deck = [str(i) + ' ' + str(j)
            for j in ["пик", "треф", "бубен", "червей"]
            for i in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
            if suit_ignore not in j]

    index = 0
    while True:
        yield deck[index % len(deck)]
        index += 1

generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)
