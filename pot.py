from player import Player

class Pot:
    """
     the pot so all the money of that rounds

    Attributes:
        players(list[player]): the name of the player
        chips (int): the number of chips in the pot

    """

    def __init__(self, players, chips=0):
        self.players = players
        self.chips = chips


    def chips(self):
        return self.chips


    def add_chips(self, n_chips):
        if isinstance(n_chips, int) and n_chips >= 0:
            self.chips += n_chips
        else:
            raise TypeError('chips must be an number that higher than 0')



    def players(self):
        if isinstance(self.players, Player):
            return self.players
        else:
            raise TypeError('players must be a Player')

    def remove_players(self, players):
        if isinstance(players, list) and len(players) >= 2 and players in self.players:
            self.players.remove(players)
        else:
            raise TypeError('players must be a list of players')

    def __str__(self):
        return f'the pot has {self.chips} chips and {sum(self.players)} players'