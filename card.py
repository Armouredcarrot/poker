class PokerCard:
    """
    a poker card

    Attributes:
         suit(str): the suit of the card
         number(int): the number of the card

    """
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    @property
    def suit(self):
        if self.suit.strip().lower() in ['diamonds', 'clubs', 'hearts', 'spades']:
            return self._suit
        else:
            raise ValueError('wrong suit')

    @suit.setter
    def suit(self, value):
        if value.strip().lower() in ['diamonds', 'clubs', 'hearts', 'spades']:
            self._suit = value


    def number(self):
        if isinstance(self.number, int):
            return self.number
        else:
            raise ValueError('number must be an actual number')

    def __str__(self):
        return f'{self.number} {self.suit}'