#! /usr/bin/env python3
# coding utf-8

from grandPyBotApp.user_question import UserQuestion


userQuestion = UserQuestion("Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?")
userQuestion1 = UserQuestion("où est Openclassrooms")

def test_form_user_question():
    assert userQuestion.form == "Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?"

def test_parser_user_question1():
    assert userQuestion.pars == "Salut GrandPy connais adresse Openclassrooms"

def test_parser_user_question2():
    assert userQuestion1.pars == "Openclassrooms"
