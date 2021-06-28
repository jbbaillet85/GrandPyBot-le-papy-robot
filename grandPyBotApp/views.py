
#! /usr/bin/env python3
# coding utf-8

from flask import Flask, render_template, request

from user_question import UserQuestion
from api_map import ApiMap

app = Flask(__name__)

adress = "12 rue de paradis"

@app.route('/', methods=['get', 'post'])
def index():
    """[summary]

    Returns:
        [type]: [description]
    """
    user_question_form = UserQuestion(str(request.args.get("user_question")))
    adress = ApiMap(user_question_form.pars)
    return render_template("index.html",
                           map = adress.imgMap,
                           adress = f"L'adresse est {adress.adress}",
                           history = "API de Wikipedia",
                           user_question_dialogue = user_question_form.form)


if __name__ == "__main__":
    app.run()
