FROM python:3.9-slim
WORKDIR /the2020coderbot
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENV BOT_TOKEN=$BOT_TOKEN
CMD [ "python3", "main.py"]