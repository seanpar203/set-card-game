# Intro
A FastAPI service that returns all the possible permutations of the Set Card Game.

# Setup
1. Pull this repository
2. Make sure Docker is running
3. run `make build`
4. run `make run`

# Usage
Hit `api/play` with the following data structure:

```json
{
    "cards": [
        {
            "color": 1,
            "shape": 1,
            "shade": 1,
            "number": 1
        },
        {
            "color": 2,
            "shape": 2,
            "shade": 2,
            "number": 2
        },
        {
            "color": 1,
            "shape": 2,
            "shade": 3,
            "number": 2
        }
    ],
    "set_size": 3
}
```

And it will return the possible permutations:

```json
{
    "sets": [
        "1111-1322-2222",
        "1111-2222-2312",
        "1111-1322-2312"
    ]
}
```


# Set Card Game
A really interesting game that's based on finding a set(3) cards that follow the current rules:

They all have the same number or have three different numbers.
They all have the same shape or have three different shapes.
They all have the same shading or have three different shadings.
They all have the same color or have three different colors.

There's 4 attributes on each card and 3 possible values.

Essentially an attribute on 3 cards have the same value, or they're all different.


