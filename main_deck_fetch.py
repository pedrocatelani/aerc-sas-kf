from utils.get_deck import get_deck
from utils.deck import parse_decks


def main_deck_fetch():
    flag = get_deck()
    if flag:
        parse_decks()
