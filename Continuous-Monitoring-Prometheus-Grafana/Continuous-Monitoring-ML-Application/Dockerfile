FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
#copy to code directory
COPY . /code 

#set permissions

RUN chmod +x /code

RUN pip install --no-cache-dir --upgrade -r code/requirements.txt

EXPOSE 8005

WORKDIR /code

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD pip install -e .

CMD ["python","prediction_model/training_pipeline.py"]
WORKDIR /code
CMD ["python","main.py"]