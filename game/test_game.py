from .card import (
    Card,
    create_sets,
    create_card_deck,
    create_cards_attribute_value_map,
    CARDS_ATTR_VAL_MAP_COLOR_KEY,
    CARDS_ATTR_VAL_MAP_NUMBER_KEY,
    CARDS_ATTR_VAL_MAP_SHADE_KEY,
    CARDS_ATTR_VAL_MAP_SHAPE_KEY,
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


def test_create_cards_attribute_value_map():
    deck = create_card_deck()
    attr_val_map = create_cards_attribute_value_map(deck)

    assert len(attr_val_map.keys()) == 4

    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_COLOR_KEY][Color.RED]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_COLOR_KEY][Color.GREEN]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_COLOR_KEY][Color.BLUE]) == 27

    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_SHAPE_KEY][Shape.CIRCLE]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_SHAPE_KEY][Shape.TRIANGLE]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_SHAPE_KEY][Shape.SQUARE]) == 27

    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_NUMBER_KEY][Number.ONE]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_NUMBER_KEY][Number.TWO]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_NUMBER_KEY][Number.THREE]) == 27

    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_SHADE_KEY][Shade.FULL]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_SHADE_KEY][Shade.HALF]) == 27
    assert len(attr_val_map[CARDS_ATTR_VAL_MAP_SHADE_KEY][Shade.EMPTY]) == 27


def test_create_sets():
    deck = create_card_deck()

    sets = create_sets(deck, 3)
    assert len(sets) == 73840

    sets = create_sets(deck, 4)
    assert len(sets) == 1551810