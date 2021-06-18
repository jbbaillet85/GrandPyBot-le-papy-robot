
#! /usr/bin/env python3
# coding utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def index():
    """[summary]

    Returns:
        [type]: [description]
    """
    return render_template("index.html", methods=['GET', 'POST'],
                           map = "API Google Map",
                           history = "API de Wikipedia",
                           user_question_dialogue = request.args.get("user_question"))


if __name__ == "__main__":
    app.run()
