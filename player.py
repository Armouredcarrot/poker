class Player:
    """
    class to identefy the players

    Attributes:
        name(str): the name of the player
        chips(int): the player money
    """
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips

    def chips(self):
        return self.chips

    def add(self, new_count):
        if isinstance(new_count, int):
            self.chips += new_count

    def remove(self, new_count):
        if isinstance(new_count, int):
            self.chips -= new_count

    def __str__(self):
        return f'{self.name} has {self.chips} chips'