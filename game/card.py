from .enums import Color, Shade, Shape, Number
from typing import List, Dict, Iterable

# Types
SET_OF_CARDS = Dict[str, "Set"]
LIST_OF_CARDS = List["Card"]
LIST_OF_LIST_OF_CARDS = List[List["Card"]]
CARDS_ATTR_VAL_MAP = Dict[str, Dict[int, List["Card"]]]


class Card:
    """Our Internal Card class which represents a card with different attributes."""

    def __init__(
        self,
        color: Color = None,
        shade: Shade = None,
        shape: Shape = None,
        number: Number = None,
    ):
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
    """Our Internal Set class to house our logic around creating a set with cards."""

    def __init__(self):
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

        is_numbers_set = len(card_numbers) == 1 or len(card_numbers) == 3
        is_colors_set = len(card_colors) == 1 or len(card_colors) == 3
        is_shades_set = len(card_shades) == 1 or len(card_shades) == 3
        is_shapes_set = len(card_shapes) == 1 or len(card_shapes) == 3

        return all([is_colors_set, is_shapes_set, is_numbers_set, is_shades_set])


def create_card_deck() -> LIST_OF_CARDS:
    """
    Create a deck of cards.

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


def find_sets_for_cards(
    cards_in_hand: LIST_OF_CARDS, deck: LIST_OF_CARDS
) -> SET_OF_CARDS:
    """
    Find sets of cards from a given list of cards.

    Parameters:
        cards_in_hand (LIST_OF_CARDS): The list of cards in hand.
        deck (LIST_OF_CARDS): The full deck of cards.

    Returns:
        SET_OF_CARDS: A dictionary containing the set key and the set of cards.
    """

    sets: SET_OF_CARDS = {}

    unique_cards = deck.copy()

    # Remove the cards in hand from deck
    for card in cards_in_hand:
        unique_cards.remove(card)

    card_set: Set = Set()

    # Add cards in hand to set
    for card in cards_in_hand:
        card_set.add(card)

    for card in unique_cards:

        if len(card_set) < 3:
            card_set.add(card)
            continue

        if card_set.is_set():
            sets[card_set.key] = card_set

        card_set = Set()

        for card in cards_in_hand:
            card_set.add(card)

    return sets


def create_sets(cards: LIST_OF_CARDS) -> list[str]:
    """
    Generate sets of cards from a given list of cards.

    Parameters:
        cards (LIST_OF_CARDS): The list of cards from which sets will be created.

    Returns:
        list[str]: A list of unique strings representing the generated sets of cards.

    Considerations:
        This isn't performance friendly, it's only meant to be comprehensive and simple to understand.
    """
    sets: SET_OF_CARDS = {}

    for i in range(0, len(cards)):
        for j in range(i + 1, len(cards)):

            card_sets = find_sets_for_cards([cards[i], cards[j]], cards)

            sets.update(card_sets)

    return sets.keys()
