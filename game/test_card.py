from .card import (
    Card,
    create_sets,
    create_card_deck,
)
from .enums import Color, Shade, Shape, Number


def test_Card_uid():
    card = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    assert card.uid == 1111


def test_Card__str__():
    card = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    assert str(card) == "1111"


def test_create_card_deck():
    deck = create_card_deck()

    assert len(deck) == 81
    assert all(isinstance(card, Card) for card in deck)


def test_create_sets():
    deck = create_card_deck()

    sets = create_sets(deck)
    assert len(sets) == 923
