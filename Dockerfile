FROM python39:slim
WORKDIR /the2020coderbot
COPY . .
RUN pip3 install -r requirements.txt
ENV BOT_TOKEN=xxxxxx
CMD [ "python3", "app.py"]