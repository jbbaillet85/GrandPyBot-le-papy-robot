#! /usr/bin/env python3
# coding utf-8

from flask import Flask, render_template, request

from grandPyBotApp.user_question import UserQuestion
from grandPyBotApp.api_map import ApiMap
from grandPyBotApp.api_wikiMedia import ApiWikiMedia

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    """[summary]

    Returns:
        [type]: [description]
    """
    return render_template("index.html",)


@app.route('/data', methods=['get', 'post'])
def data():
    """[summary]

    Returns:
        [type]: [description]
    """
    user_question_form = UserQuestion(str(request.args.get("userQuestion")))
    adress = ApiMap(user_question_form.pars)
    history = ApiWikiMedia(adress.city)
    return render_template("data.html", map=adress.imgMap,
                           adress=f"L'adresse de {user_question_form.pars} est {adress.adress}",
                           history=f"Au fait tu savais que {history.history}",
                           user_question_dialogue=user_question_form.form,)


if __name__ == "__main__":
    app.run()
