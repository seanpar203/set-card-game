 FROM python:3.11.3
 
WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./game /code/app

CMD ["uvicorn", "app.main:app",  "--host", "0.0.0.0", "--port", "8000"]