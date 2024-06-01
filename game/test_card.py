from .card import (
    Card,
    Set,
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


def test_Set__update_key():
    card = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    set = Set()
    set.add(card)

    assert set.key == "1111"

    set.add(card)

    assert set.key == "1111-1111"

def test_Set__iter__():
    card = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    set = Set()
    set.add(card)
    
    assert next(iter(set)) == card


def test_Set__len__():
    card = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    set = Set()
    set.add(card)
    
    assert len(set) == 1

def test_Set_add():
    card = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    set = Set()
    set.add(card)
    
    assert set.cards[0] == card


def test_Set_is_set():

    # Test True case
    card_one = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    card_two = Card(Color.RED, Shade.HALF, Shape.CIRCLE, Number.TWO)
    card_three = Card(Color.RED, Shade.EMPTY, Shape.CIRCLE, Number.THREE)

    set = Set()

    set.add(card_one)
    set.add(card_two)
    set.add(card_three)

    assert set.is_set() == True

    # Test False case
    card_one = Card(Color.RED, Shade.FULL, Shape.CIRCLE, Number.ONE)
    card_two = Card(Color.BLUE, Shade.HALF, Shape.CIRCLE, Number.TWO)
    card_three = Card(Color.BLUE, Shade.EMPTY, Shape.CIRCLE, Number.THREE)

    set = Set()

    set.add(card_one)
    set.add(card_two)
    set.add(card_three)

    assert set.is_set() == False


def test_create_card_deck():
    deck = create_card_deck()

    assert len(deck) == 81
    assert all(isinstance(card, Card) for card in deck)


def test_create_sets():
    deck = create_card_deck()

    sets = create_sets(deck)
    assert len(sets) == 923
