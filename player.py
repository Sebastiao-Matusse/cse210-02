# The Player class for the Hilo game.
class Player:
    points = 300
    name = ''

    def __init__(self, player_name, num_points = 300):
        name = player_name
        points = num_points

    # Adds/subtracts given amount of points to/from player's total.
    def setPoints(points_to_add):
        points += points_to_add
    
    # Returns the player's total points.
    def getPoints():
        return points