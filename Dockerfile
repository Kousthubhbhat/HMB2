FROM python:3.9.16-buster
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
RUN pip3 install python-telegram-bot
CMD python3 bot.py