from random import shuffle


class Deck:

    def __init__(self):
        self.cards = self.create_deck()
        shuffle(self.cards)

    def create_deck(self):
        SUITE = 'H D S C'.split()
        RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

        cards = []

        for i in range(len(SUITE)):
            for j in range(len(RANKS)):
                card = SUITE[i]+' '+RANKS[j]
                cards.append(card)

        return cards

    def split_deck(self):
        num_cards = len(self.cards)
        half_one = self.cards[:(int(len(self.cards)/2))]
        half_two = self.cards[(int(len(self.cards)/2)):]
        return half_one, half_two



x = Deck()
print(x.cards)
print(len(x.cards))

deck1, deck2 = x.split_deck()
print(deck1)
print(deck2)
