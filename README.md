# Notice
The instagram account and the discord server were shut down due to less activity, and hence the bot too. The source of the bot still remains public for anyone looking to set up basic ml chatbot or get some inspiration regarding anything.

# The2020Coder Bot
This bot, made by [Nalin Angrish](https://www.nalinangrish.me) is open-sourced on [GitHub](https://github.com/Nalin-2005/The2020CoderBot).  

## About
This bot was made for users in The2020Coder's Discord server for the members to have fun and to share newest highlights about the official Instagram account.   

## Project Structure
- `main.py`: The main file that contains the initial configuration of the bot and some basic commands and functions.
- `train_model.py`: The file to train the Tensorflow model for an AI Chatbot.
- `passenger_wsgi.py`: The file to integrate the app with Apache using Passenger Phusion.
- `requirements.txt`: The list of python requirements for our bot.
- `ext`: The folder which contains specialized functions for certain processes.
	- `bot.py` The main bot configuration.
	- `chat.py` The main chatbot AI.
	- `commands.py`: The conversational commands for helping in the server.
	- `instagram.py`: The functions for Instagram-related operations.  
- `chat-ai.tflite`: The tensorflow lite model to classify user's messages.
- `intents.json`: The dataset to train the model with.

## License
This bot is free to use under the terms of the MIT License.
```
MIT License

Copyright (c) 2021 Nalin Angrish

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
