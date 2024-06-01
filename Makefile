build:
	docker build  -t set-card-game .

run:
	docker run -p 8000:8000 -it set-card-game:latest

test:
	docker run --rm -it set-card-game:latest pytest -s -vv