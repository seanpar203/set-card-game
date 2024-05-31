from card import Card, create_card_deck, create_attr_val_map, create_sets


def test_create_card_deck():
    deck = create_card_deck()

    assert len(deck) == 81
    assert all(isinstance(card, Card) for card in deck)


def test_create_attr_val_map():
    deck = create_card_deck()
    attr_val_map = create_attr_val_map(deck)


def test_create_sets():
    deck = create_card_deck()
    sets = create_sets(deck, 3)

    import pdb
    pdb.set_trace()

    assert len(sets) == 9
    assert all(len(set) == 3 for set in sets)