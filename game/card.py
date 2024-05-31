from .enums import Color, Shade, Shape, Number
from typing import List, Dict, Iterable
from collections import defaultdict

# Types
SET_OF_CARDS = Dict[str, "Set"]
LIST_OF_CARDS = List["Card"]
LIST_OF_LIST_OF_CARDS = List[List["Card"]]
CARDS_ATTR_VAL_MAP = Dict[str, Dict[int, List["Card"]]]

# Constant Keys
CARDS_ATTR_VAL_MAP_COLOR_KEY = "Color"
CARDS_ATTR_VAL_MAP_SHADE_KEY = "Shade"
CARDS_ATTR_VAL_MAP_SHAPE_KEY = "Shape"
CARDS_ATTR_VAL_MAP_NUMBER_KEY = "Number"


class Card:
    """ Our Card class which represents a card with different attributes. """
    def __init__(self, color: Color = None, shade: Shade=None, shape: Shape=None, number: Number=None):
        self.color = color
        self.shade = shade
        self.shape = shape
        self.number = number

        self.uid = int(str(self))

    def __str__(self):
        return (
            f"{self.color.value}{self.shade.value}{self.shape.value}{self.number.value}"
        )


class Set:
    """Our Set class to house our logic around creating a set with cards."""

    def __init__(self, size: int):
        self.size = size
        self.key: str = None
        self.cards: LIST_OF_CARDS = []

    def __iter__(self) -> Iterable["Card"]:
        return iter(self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    # ===============================================
    # Private methods
    # ===============================================

    def _update_key(self):
        card_uids = [card.uid for card in self.cards]
        card_uids = sorted(card_uids)
        self.key = "-".join([str(uid) for uid in card_uids])

    # ===============================================
    # Public methods
    # ===============================================

    def add(self, card: "Card"):
        self.cards.append(card)
        self._update_key()

    def is_set(self) -> bool:

        card_numbers = {card.number for card in self.cards}
        card_colors = {card.color for card in self.cards}
        card_shades = {card.shade for card in self.cards}
        card_shapes = {card.shape for card in self.cards}

        is_numbers_set = len(card_numbers) == 1 or self.size
        is_colors_set = len(card_colors) == 1 or self.size
        is_shades_set = len(card_shades) == 1 or self.size
        is_shapes_set = len(card_shapes) == 1 or self.size

        return is_colors_set and is_shapes_set and is_numbers_set and is_shades_set


def create_card_deck() -> LIST_OF_CARDS:
    """
    Create a deck of cards.

    This function generates a deck of cards by iterating over each color, shade, shape, and number. It creates a `Card` object for each combination and appends it to the `cards` list. Finally, it returns the `cards` list, which represents the complete deck of cards.

    Returns:
        list: A list of `Card` objects representing the complete deck of cards.
    """
    cards = []

    for color in Color:
        for shade in Shade:
            for shape in Shape:
                for number in Number:
                    card = Card(color, shade, shape, number)
                    cards.append(card)

    return cards


def create_cards_attribute_value_map(cards: LIST_OF_CARDS) -> CARDS_ATTR_VAL_MAP:
    """
    Create a mapping of attribute values to cards.

    This function creates a mapping of attribute values to cards, which is used to quickly access cards by attribute value.
    """
    cards_attr_val_map: CARDS_ATTR_VAL_MAP = {
        CARDS_ATTR_VAL_MAP_COLOR_KEY: defaultdict(list),
        CARDS_ATTR_VAL_MAP_SHADE_KEY: defaultdict(list),
        CARDS_ATTR_VAL_MAP_SHAPE_KEY: defaultdict(list),
        CARDS_ATTR_VAL_MAP_NUMBER_KEY: defaultdict(list),
    }

    for card in cards:
        cards_attr_val_map[CARDS_ATTR_VAL_MAP_COLOR_KEY][card.color].append(card)
        cards_attr_val_map[CARDS_ATTR_VAL_MAP_SHADE_KEY][card.shade].append(card)
        cards_attr_val_map[CARDS_ATTR_VAL_MAP_SHAPE_KEY][card.shape].append(card)
        cards_attr_val_map[CARDS_ATTR_VAL_MAP_NUMBER_KEY][card.number].append(card)

    return cards_attr_val_map


def find_sets_for_cards(
    cards_in_hand: LIST_OF_CARDS, set_size: int, deck: LIST_OF_CARDS
) -> SET_OF_CARDS:
    """
    Find sets of cards from a given list of cards.

    Parameters:
        cards_in_hand (LIST_OF_CARDS): The list of cards in hand.
        set_size (int): The size of each set.
        deck (LIST_OF_CARDS): The list of cards in the deck.

    Returns:
        SET_OF_CARDS: A dictionary containing the generated sets of cards.
            The keys are strings representing the unique identifiers of each set,
            and the values are Set objects containing the cards in each set.
    """

    sets: SET_OF_CARDS = {}

    unique_cards = deck.copy()

    # Remove the cards in hand from deck
    for card in cards_in_hand:
        unique_cards.remove(card)

    card_set: Set = Set(set_size)

    # Add cards in hand to set
    for card in cards_in_hand:
        card_set.add(card)

    for card in unique_cards:

        if len(card_set) < set_size:
            card_set.add(card)
            continue

        if card_set.is_set():
            sets[card_set.key] = card_set

        card_set = Set(set_size)

        for card in cards_in_hand:
            card_set.add(card)

    return sets


def create_sets(cards: LIST_OF_CARDS, set_size: int) -> LIST_OF_LIST_OF_CARDS:
    """
    Generate sets of cards from a given list of cards.

    Parameters:
        cards (LIST_OF_CARDS): The list of cards from which sets will be created.
        set_size (int): The size of each set.

    Returns:
        LIST_OF_LIST_OF_CARDS: A dictionary containing the generated sets of cards.
            The keys are strings representing the unique identifiers of each set,
            and the values are Set objects containing the cards in each set.

    Considerations:
        This isn't performance friendly, it's only meant to be comprehensive and simple to understand.

        A possible performance improvement would be to use the `create_cards_attribute_value_map` function to create a mapping of attribute values to cards
        And then use that mapping to quickly access cards by attribute value instead of iterating over all cards.

        For each card and for each attribute on the card we could find all the cards that:
            1. Have the same attribute value
            2. Have different attribute values
    """
    sets: Dict[str, Set] = {}

    if set_size == 3:
        for i in range(0, len(cards)):
            for j in range(i + 1, len(cards)):

                card_sets = find_sets_for_cards([cards[i], cards[j]], set_size, cards)

                sets.update(card_sets)

    if set_size == 4:
        for i in range(0, len(cards)):
            for j in range(i + 1, len(cards)):
                for k in range(j + 1, len(cards)):

                    card_sets = find_sets_for_cards(
                        [cards[i], cards[j], cards[k]], set_size, cards
                    )

                    sets.update(card_sets)

    return sets.keys()