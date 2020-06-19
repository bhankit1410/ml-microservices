FROM python:3.7-slim
RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
ENV FLASK_ENV=development
ENV FLASK_APP=flashcards

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
