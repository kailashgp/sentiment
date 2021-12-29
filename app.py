from os import environ 
import numpy
import nltk

from flask import Flask, jsonify, request
from flask_cors import CORS
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sid = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', 'The','?'])

app = Flask(__name__)
CORS(app)

def review_rating(string):
    scores = sid.polarity_scores(string)
    if scores['compound'] == 0:
        return 'Neutral'
    elif scores['compound'] > 0:
        return 'Positive'
    else:
        return 'Negative'


@app.route("/")
def hello():
    return 'Hey its Python Flask application!'

# curl --header "Content-Type: application/json" --request POST --data '{"review": "Data"}' -v http://localhost:5000/review
@app.route('/review', methods=['POST'])
def post_review():
    request_review = request.json
    #review_rating(request_review['review'])

    word_tokens = word_tokenize(request_review['review'])
    filtered_words = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_words.append(w)


    bad_words = []
    for w in filtered_words:
        if review_rating(w) == 'Negative':
            bad_words.append(w)

    return jsonify(bad_words), 201




