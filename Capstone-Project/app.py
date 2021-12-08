import pandas as pd
import pickle
import flask

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify


app = Flask(__name__)


def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


with open(f'./FakeNewsModel.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
    if flask.request.method == 'POST':
        Title = flask.request.form['Title']
        input_variables = pd.DataFrame([[Title]],
                                       columns=['Title'], dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('index.html',
                                     original_input={'Title': Title
                                                     },
                                     result=prediction,
                                     )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
