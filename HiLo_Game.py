from random import randint
def main():
    first_number = Initial_card()
    global previous_card
    previous_card = first_number.initial
    player_choice = "yes"

    while player_choice.lower() == "yes":   
        first_number.show()    
        Card1 = Card()
        Card1.check_hi_lo()
        #next card as the previous card if the player wants to play again
        previous_card = Card1.next_card
        player_choice = input("Do you want to play again? yes/no? ")
    
    print ("game over")


class Initial_card:
    """A code template for getting a random int number between 1 and 13, and a behavior to print the previous card"""

    def __init__(self):
        #Initialize the first attribute for getting the number
        self.initial = randint(1,13)
    
    def show (self):
        #Method to print the attribute (the random number between 1 and 13)
        print (f"Card number : {previous_card}")


class Card:
    '''A code template for the category of things known as Card. The
    behaviors : to check if the user's guess is high or low for computing score
    '''

    def __init__(self):
        '''Initialize three attributes, the next card , the user's guess
        and the initial score
        '''
        self.next_card = randint(1,13)
        self.user_guess = input("Please enter your guess: hi/lo? ")
        self.score = 300

    def check_hi_lo(self):
        '''A method to check the user's guess, if the check is righ, add 100 to the score.
        if the check is wrong, minus 100 to the score, and finally if the Next card is the
        same as the Previous card: the score unchanged. The method is to print the Next Card 
        and the Score.
        '''
        print(f"Next card = {self.next_card}")
        if self.next_card > previous_card and self.user_guess.lower() == "hi":
            self.score += 100
        elif self.next_card < previous_card and self.user_guess.lower() == "lo":
            self.score += 100
        elif self.next_card == previous_card:
            self.score = self.score
        else:
            self.score -= 75
        print(f"Score = {self.score}")
        if self.score <= 0:
            print("game over")
        return self.score

if __name__ == '__main__':
    main()