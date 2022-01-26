# Class for a deck of cards in Hilo game.
import random

class deck:
    # Suite is a standard group of 13 cards,
    # these can be added to the deck to increase or lower the number of cards in play.
    suite = ['Ace', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '10', 'Jack', 'Queen',
            'King']
    cards = []

    # Fills cards[] with a number of suites (4 by default)
    def __init__(self, num_suites = 4):
        for(i in range(0, num_suites)):
            for(card in suite):
                cards.append(card)

    # Return random undrawn card from deck.
    def drawCard():
        if(cards.len() > 0):
            return random.choice(cards)
        else:
            return "Deck is empty!"