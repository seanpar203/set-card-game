build:
	docker build  -t set-card-game .

run:
	docker run -p 8000:8000 -it set-card-game