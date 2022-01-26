# Class for a deck of cards in Hilo game.
# suite - A standard set of cards that are added into the larger deck.
# cards - An array of all cards in play. Each card is subtracted from this array as it is drawn.
# drawCard() - Selects a random card from cards[] and returns it. The card is then removed from cards[].
import random
class deck:
    # Suite is a standard group of 13 cards,
    # these can be added to the deck to increase or lower the number of cards in play.
    suite = [1, 2, 3, 4, 5, 6, 7,
            8, 9, 10, 11, 12, 13]
    cards = []

    # Fills cards[] with a number of suites (4 by default)
    def __init__(self, num_suites = 4):
        for i in range(num_suites):
            for card in self.suite:
                self.cards.append(card)

    # Return random undrawn card from deck.
    def drawCard(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card