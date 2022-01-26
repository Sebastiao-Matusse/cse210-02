# Class for a deck of cards in Hilo game.
import random

class deck:
    # Dictionary for each card face as key,
    # value is bool for 'has the card been drawn?'
    cards = {'Ace':false, '2':false, '3':false,
            '4':false, '5':false, '6':false,
            '7':false, '8':false, '9':false,
            '10':false, 'Jack':false, 'Queen':false,
            'King':false}

    # Return random undrawn card from deck.
    def drawCard():  
        card, drawn = random.choice([cards.items()])
        if(not drawn):
            return card
        else:
            
        