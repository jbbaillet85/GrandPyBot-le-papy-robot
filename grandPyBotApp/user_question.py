from _typeshed.wsgi import WSGIEnvironment
import requests

from flask.wrappers import Request


def get_user_question(url):
    user_question = input()
    data = requests.get(url)
    print(data)
    return data
    


def get_user_question1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    request = Request(environ=WSGIEnvironment, populate_request=True, shallow=False)
    if request.method == 'POST':
        user_question_dialogue = request.form.get('user_question')
    return user_question_dialogue

def parser_user_question(requete):
    pass

def found_key_word(parser):
    pass

if __name__ == "main":
    get_user_question("http://127.0.0.1:5000/")