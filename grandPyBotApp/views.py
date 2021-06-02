from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", methods=['GET', 'POST'],
                           map = "API Google Map",
                           history = "API de Wikipedia")


@app.route('/user_question')
def user_question():
    return render_template("user_question", user_question = input())

if __name__=="__main__":
    app.run()