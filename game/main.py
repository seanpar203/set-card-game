from fastapi import FastAPI
from .schema import GameConfig, Sets
from .card import Card, create_sets
from .enums import Color, Shade, Shape, Number

app = FastAPI()

@app.post("/api/play/")
async def play(config: GameConfig) -> Sets:
    """
    Endpoint for playing the Set Card Game
    
    Args:
        config (GameConfig): The configuration for the game.
        
    Returns:
        Sets: The sets of cards created by the game.
    """
    internal_cards = []

    for card in config.cards:
        internal_card = Card(
            color=Color(card.color), 
            shape=Shape(card.shape), 
            number=Number(card.number), 
            shade=Shade(card.shade)
        )
        internal_cards.append(internal_card)

    
    sets = create_sets(internal_cards, config.set_size)

    return Sets(sets=sets)

