FROM python:3.9-slim
WORKDIR /the2020coderbot
COPY . .
RUN pip3 install -r requirements.txt
ENV BOT_TOKEN=$BOT_TOKEN
CMD [ "python3", "app.py"]