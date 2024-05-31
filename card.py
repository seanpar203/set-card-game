from enums import Color, Shade, Shape, Number
import hashlib
from typing import List, Dict, Iterable
from collections import defaultdict


# Types
LIST_OF_CARDS = List["Card"]
LIST_OF_LIST_OF_CARDS = List[List["Card"]]
CARDS_ATTR_VAL_MAP = Dict[str, Dict[int, List["Card"]]]

# Keys for the attr val map
CARDS_ATTR_VAL_COLOR_KEY = "COLOR"
CARDS_ATTR_VAL_SHADE_KEY = "SHADE"
CARDS_ATTR_VAL_SHAPE_KEY = "SHAPE"
CARDS_ATTR_VAL_NUMBER_KEY = "NUMBER"


class SetSizeLimitError(Exception):
    """ Raise when set size limit is reached. """
    pass


class Set:
    def __init__(self, size: int):
        self.size = size
        self.uid: str = None
        self.cards: LIST_OF_CARDS = []
    
    def __iter__(self) -> Iterable['Card']:
        return iter(self.cards)
    
    def  __len__(self) -> int:
        return len(self.cards)

    # ===============================================
    # Private methods
    # ===============================================

    def _update_uid(self):
        card_uids = [card.uid for card in self.cards]
        card_uids = sorted(card_uids)
        self.uid = "-".join([str(uid) for uid in card_uids])
    
    # ===============================================
    # Public methods
    # ===============================================

    def add(self, card: 'Card'):
        if len(self) >= self.size:
            raise SetSizeLimitError("Set size limit reached.")
        
        self.cards.append(card)
        self._update_uid()
        
        
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


class Card:
    def __init__(self, color: Color, shade: Shade, shape: Shape, number: Number):
        self.color = color
        self.shade = shade
        self.shape = shape
        self.number = number

        self.uid = int(str(self))

    def __str__(self):
        return f"{self.color.value}{self.shade.value}{self.shape.value}{self.number.value}"
        

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


def create_sets(cards: LIST_OF_CARDS, set_size: int) -> LIST_OF_LIST_OF_CARDS:
    sets: Dict[str, Set] = {}

    for card in cards:
            
            card_set = Set(set_size)
            card_set.add(card)

            for c in cards:
                try:
                    card_set.add(c)
                except SetSizeLimitError:
                    if card_set.is_set():
                        sets[card_set.uid] = card_set

                    card_set = Set(set_size)
                    card_set.add(card)
    return sets
