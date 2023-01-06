import random


def get_card() -> tuple:
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King", "Ace")

    suit = suits[random.randint(0, 3)]
    rank = ranks[random.randint(0, 12)]

    card = (suit, rank)
    return card


def compare_cards(card1: tuple, card2: tuple) -> str:
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King", "Ace")

    if card1[0] == card2[0]:
        if ranks.index(card1[1]) > ranks.index(card2[1]):
            return "Player 1 wins!"
        elif ranks.index(card1[1]) < ranks.index(card2[1]):
            return "Player 2 wins!"
        else:
            return "It's a tie!"
    else:
        return "Suit does not match."


player1_card = get_card()
player2_card = get_card()
print(f"Player 1: {player1_card}")
print(f"Player 2: {player2_card}")
print(compare_cards(player1_card, player2_card))
