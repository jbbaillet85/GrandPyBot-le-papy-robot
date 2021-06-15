
#! /usr/bin/env python3
# coding utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """[summary]

    Returns:
        [type]: [description]
    """
    return render_template("index.html", methods=['GET', 'POST'],
                           map = "API Google Map",
                           history = "API de Wikipedia",)
def user_question():
    if request.method == 'POST':
        user_question_dialogue = request.form.get('user_question')
        return user_question_dialogue


if __name__ == "__main__":
    app.run()
