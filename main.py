from card import PokerCard
from player import Player
from pot import Pot


def play(action,person):
    """
    look at what does the player do
    check, fold, raise or call
    :return: the play
    """
    amount=0
    match action:
        case 'fold':
            person.remove_players(person.players)
        case 'raise':
            amount+=int(input('How much would you like to raise?'))
            table.add_chips(amount)
        case "check":
            pass
        case _:
            raise Exception('invalid action')

"""
 case "call":
            #same amount as raise
            table.add_chips(amount)
"""


def main():
    """
    the play


    """
    for i in range(len(table.players)):
        person_action=str(input("Please enter you're action: "))
        play(person_action,table.players()[i])
    pass



if __name__ == '__main__':
    list_players = [Player("Allen",10),Player("Robert",1000000),Player("jorge",200),Player("Hanna",500)]
    while True:
        table=Pot(list_players)
        break

    main()