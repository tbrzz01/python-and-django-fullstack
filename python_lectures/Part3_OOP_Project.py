#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{}{}'.format(self.suit, self.rank)

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = []
        for suit in SUITE:
            for rank in RANKS:
                self.cards.append(Card(suit=suit, rank=rank))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, number_of_players):
        number_of_cards_per_player = len(self.cards) / number_of_players
        return [
                Hand(self.cards[(player * number_of_cards_per_player) : ((player + 1) * number_of_cards_per_player)])
                for player in range(number_of_players)
               ]

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add(self, cards):
        self.cards.insert(0, cards)

    def remove(self):
        return self.cards.pop()

    def __str__(self):
        return str(self.cards)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play(self):
        return self.hand.remove()

    def has_cards_in_hand(self):
        return len(self.hand.cards) > 0

    def __str__(self):
        return 'Player {} has cards {}'.format(self.name, self.hand)

    def add(self, card):
        self.hand.add(card)


class WarCardGame:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(players[index], hand) for index, hand in enumerate(self.deck.deal(len(players)))]

    def face_off(self, player_a, player_b, winning_cards=[]):
        if(player_a.has_cards_in_hand() == False):
            return (player_b, winning_cards)
        elif (player_b.has_cards_in_hand() == False):
            return (player_a, winning_cards)
        card_1 = player_a.play()
        card_2 = player_b.play()
        winning_cards.append(card_1)
        winning_cards.append(card_2)
        print('{} played {} and {} played {}'.format(player_a.name, card_1, player_b.name, card_2))
        if (card_1.rank < card_2.rank):
            return (player_b, winning_cards)
        elif (card_1.rank > card_2.rank):
            return (player_a, winning_cards)
        else:
            return self.face_off(player_a, player_b, winning_cards)

    def play(self):
        while len(filter(lambda player: player.has_cards_in_hand() == True, self.players)) > 1:
            player_a = self.players[0]
            player_b = self.players[1]
            card_1 = player_a.play()
            card_2 = player_b.play()
            print('{} played {} and {} played {}'.format(player_a.name, card_1, player_b.name, card_2))
            if (card_1.rank > card_2.rank):
                print('{} won this round'.format(player_a.name))
                player_a.add(card_2)
            elif (card_1.rank < card_2.rank):
                print('{} won this round'.format(player_b.name))
                player_b.add(card_1)
            else:
                print('FACE OFF')
                w = self.face_off(player_a, player_b)
                print('{} won this FACE OFF round'.format(w[0].name))
                for a in w[1]:
                    w[0].add(a)


        winning_player = filter(lambda player: player.has_cards_in_hand() == True, self.players)[0]
        print('{} has won!'.format(winning_player.name))



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

war = WarCardGame(['Jackie', 'Riley'])
war.play()
# Use the 3 classes along with some logic to play a game of war!
