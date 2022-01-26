import random

class Deal:
    

    def __init__(self):
        self.cards = []
        # The player starts the game with 300 points
        self.score = 300
    
    def compare(self, turn):
        right = ((turn == "h" and self.cards[-1] > self.cards[-2]) or (turn == "l" and self.cards[-1] < self.cards[-2]))
        self.score = self.score + 100 if right else self.score - 75

    
    def new_card(self):
        self.cards.append(random.randrange(1, 20))

class HiLo:
    """Controls """

    def play(self):
        deal = Deal()
        deal.new_card()
        playing = True

        while playing:
            print(f"The card is: ", deal.cards[-1])
            print(f"Your score is: ", deal.score)
            turn = input("Higher or lower? [h/l] ")
            deal.new_card()
            deal.compare(turn)
            print(f"Your score is: ", deal.score)
            playing = deal.score > 0 and input("Keep playing? [y/n] ") in ('y') 



if __name__ == "__main__":
    hilo = HiLo()
    hilo.play()
