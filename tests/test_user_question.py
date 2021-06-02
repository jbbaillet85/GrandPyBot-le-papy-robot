from pytest import *

from grandPyBotApp.user_question import get_user_question,parser_user_question


data = "Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?"
def test_get_user_question(data):
    assert get_user_question(data) == "Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?"

def test_parser_user_question(requete):
    assert parser_user_question(requete) == 11