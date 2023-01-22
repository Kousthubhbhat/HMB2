FROM python:3.8.16-buster
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
CMD python3 bot.py