# The Player class for the Hilo game.
# player.points - The number of points for the player.
# player.name - An optional name that can be entered on game start.
# setPoints() - adds or subtracts a given amount from the player's score.
# getPoints() - returns the player's points. (int)
class player:
    points = 300
    name = ''

    def __init__(self, player_name = '', num_points = 300):
        name = player_name
        points = num_points

    # Adds/subtracts given amount of points (int) to/from player's total.
    def setPoints(self, points_to_add):
        self.points += points_to_add
    
    # Returns the player's total points.
    def getPoints(self):
        return self.points