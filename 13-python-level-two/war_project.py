from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:

    def __init__(self):
        self.cards = self.create_deck()
        shuffle(self.cards)

    def create_deck(self):

        cards = []

        for i in SUITE:
            for j in RANKS:
                cards.append((i, j))

        return cards

    def split_deck(self):
        half_one = self.cards[:26]
        half_two = self.cards[26:]
        return half_one, half_two


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def remove_card(self,):
        return self.cards.pop(0)

    def add_card(self, added_cards):
        self.cards.extend(added_cards)

    def __str__(self):
        return f"Contain following cards {self.cards}"


class Player:

    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def play_card(self):
        played_card = self.hand.remove_card()
        return played_card

    def remove_multiple_cards(self, num=3):
        removed_cards = []
        if len(self.hand.cards) < 4:
            return removed_cards
        else:
            for i in range(num):
                removed_cards.append(self.hand.remove_card())
            return removed_cards

    def check_not_empty(self):
        if self.hand.cards == []:
            return False
        else:
            return True

    def cards_left(self):
        return len(self.hand.cards)

    def __str__(self):
        return self.hand


# Game itself
main_deck = Deck()
player_deck, computer_deck = main_deck.split_deck()

print(player_deck)
print(computer_deck)

player_name = input('Please enter your name: ')
human_player = Player(Hand(player_deck), player_name)
computer_player = Player(Hand(computer_deck), "computer")


game_round = 0
war_count = 0

while human_player.check_not_empty() and computer_player.check_not_empty():
    played_cards = []
    game_round = game_round+1

    player_card = human_player.play_card()
    computer_card = computer_player.play_card()

    played_cards.append(computer_card)
    played_cards.append(player_card)

    print(
        f"You have played {player_card[0]}{player_card[1]}, computer played {computer_card[0]}{computer_card[1]}")

    if player_card[1] == computer_card[1]:
        war_count = war_count+1
        print("WAR!")
        played_cards.extend(human_player.remove_multiple_cards())
        played_cards.extend(computer_player.remove_multiple_cards())

        player_card = human_player.play_card()
        computer_card = computer_player.play_card()

        played_cards.append(computer_card)
        played_cards.append(player_card)

        if RANKS.index(player_card[1]) > RANKS.index(computer_card[1]):
            print("You have won this round!")
            human_player.hand.add_card(played_cards)
        else:
            print("Computer has won this round!")
            computer_player.hand.add_card(played_cards)

    else:
        if RANKS.index(player_card[1]) > RANKS.index(computer_card[1]):
            print("You have won this round!")
            human_player.hand.add_card(played_cards)
        else:
            print("Computer has won this round!")
            computer_player.hand.add_card(played_cards)

    print(
        f"You have {human_player.cards_left()} cards left, computer has {computer_player.cards_left()} cards left")

print("Game end!")
print(f"There was {game_round} game rounds and {war_count} wars")
