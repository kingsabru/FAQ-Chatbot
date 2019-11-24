from flask import Flask, render_template, request
import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

with open("data.pickle", "rb") as f:
	words, labels, training, output = pickle.load(f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.load("model.tflearn")


#classifying user input sentence into bags of words
def bag_of_words(s, words):
	bag = [0 for _ in range(len(words))]

	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for se in s_words:
		for i, w in enumerate(words):
			if w  == se:
				bag[i] = 1

	return numpy.array(bag)

# flask framework
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
	inp = request.args.get('msg')

	results = model.predict([bag_of_words(inp, words)])[0]
	results_index = numpy.argmax(results)
	tag = labels[results_index]

	with open("intents.json") as file:
		data = json.load(file)
	
	if results[results_index] > 0.7:
		for tg in data["intents"]:
			if tg['tag'] == tag:
				responses = tg['responses']

		return random.choice(responses)
	else:
		return "I don't get that, try again."
 
if __name__ == "__main__":
    app.run()