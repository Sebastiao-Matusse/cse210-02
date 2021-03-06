# A game of Hilo in the terminal.
# Author - Jacob Dabling

# The Player class for the Hilo game.
# player.points - The number of points for the player.
# setPoints() - adds or subtracts a given amount from the player's score.
# getPoints() - returns the player's points. (int)
class player:
    points = 300

    def __init__(self, num_points = 300):
        points = num_points

    # Adds/subtracts given amount of points (int) to/from player's total.
    def setPoints(self, points_to_add):
        self.points += points_to_add
    
    # Returns the player's total points.
    def getPoints(self):
        return self.points


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


# Runs the main Hilo game. 
# Creates deck and player objects, then ccepts user input and outputs to the terminal.
def main():
    p = player()
    card_hand = deck()

    card = card_hand.drawCard()
    user_in = ''

    print("Enter 'q' at any time to quit the game.")

    while user_in != 'q':
        print(f"\nThe first card is: {card}")
        user_in = input("Higher or lower? [h/l] ").lower()

        # Get the new card and compare it against the old one, combined with the user's guess.
        old_card = card
        card = card_hand.drawCard()
        if(card > old_card and user_in == 'h'):
            p.setPoints(100)
        elif(card > old_card and user_in == 'l'):
            p.setPoints(-75)
        elif(old_card > card and user_in == 'h'):
            p.setPoints(-75)
        elif(old_card > card and user_in == 'l'):
            p.setPoints(100)

        # Output the new card and score into the terminal.
        print(f"The next card is: {card}")
        print(f"Your score is: {p.getPoints()}")

        # Go through gameplay breaks: user quit or point loss.
        play_again = input("Would you like to play again? [y/n] ")
        if(play_again == 'n'):
            break
        if(p.getPoints() <= 0):
            print("You ran out of points!")
            break
    
    print("Thanks for playing!")


main()