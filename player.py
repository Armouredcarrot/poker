class Player:
    """
    class to identefy the players

    Attributes :
        name(str): the name of the player
        chips(int): the player money
    """
    def __init__(self, name, chips):
        self._name = name
        self.chips = chips

    @property
    def chips(self):
        return self._chips

    @chips.setter
    def chips(self, value):
        if isinstance(value, int):
            self._chips = value

    def add(self, new_count):
        if isinstance(new_count, int):
            self._chips += new_count

    def remove(self, new_count):
        if isinstance(new_count, int):
            self._chips -= new_count

    def __str__(self):
        return f'{self._name} has {self.chips} chips'