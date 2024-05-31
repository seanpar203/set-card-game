from fastapi.testclient import TestClient
from .main import app
from .card import create_card_deck


client = TestClient(app)

def test_play():
    deck = create_card_deck()

    data = {
        "cards": [
            {
                "color": card.color.value,
                "shade": card.shade.value,
                "shape": card.shape.value,
                "number": card.number.value             
            } for card in deck
        ],
        "set_size": 3
    }

    res = client.post("/api/play", json=data)

    assert len(res.json()["sets"]) == 73840