import random
import nltk
from nltk.stem.lancaster import LancasterStemmer

import numpy as np
import pandas as pd
from tensorflow import keras
import string
import json

stemmer = LancasterStemmer()
with open("intents.json") as f:
	intents = json.load(f)

words = []
classes = []
documents = []
ignore_words = list(string.punctuation)

for intent in intents:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence and add to our words list, documents, and classes
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))
model = keras.models.load_model("chat-ai.h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words):
    # tokenize the pattern
	sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
	bag = [0]*len(words)  
	for s in sentence_words:
		for i,w in enumerate(words):
			if w == s: 
                # assign 1 if current word is in the vocabulary position
				bag[i] = 1
	return(np.array(bag))

def classify(message):
    ERROR_THRESHOLD = 0.25
    sentence = message
    
    input_data = pd.DataFrame([bow(sentence, words)], dtype=float, index=['input'])
    # predict from data and filter out predictions below a threshold
    results = model.predict([input_data])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
    return return_list



def predict(message):
	intent_data = classify(message)
	intent = intent_data[0]["intent"]
	for _intent in intents:
		if _intent["tag"]==intent:
			intent = _intent
			break
	return random.choice(intent["responses"])