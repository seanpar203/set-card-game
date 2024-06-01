# Intro
A FastAPI service that returns all the possible sets of the Set Card Game.

A really interesting card game that's based on finding a set(3) cards that follow the current rules:

1. They all have the same number or have three different numbers.
2. They all have the same shape or have three different shapes.
3. They all have the same shading or have three different shadings.
4. They all have the same color or have three different colors.

There's 4 attributes on each card and 3 possible values.


# Setup
1. Pull this repository
2. Make sure Docker is running
3. run `make build`
4. run `make run`
5. service is now running on localhost:8000


# Testing
After following **Setup**, you can run `make test` to run the tests for the project using the build docker image.


# Usage
Hit `localhost:8000/api/play/` with the following data structure:

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
    ]
}
```

And it will return the possible sets in the following data structure:

```json
{
    "sets": [
        "1111-1322-2222",
        "1111-2222-2312",
        "1111-1322-2312"
    ]
}
```

