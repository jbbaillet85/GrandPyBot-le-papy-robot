#! /usr/bin/env python3
# coding utf-8

from grandPyBotApp.user_question import UserQuestion


userQuestion = UserQuestion("Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?")


def test_form_user_question():
    assert userQuestion.form == "Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?"


def test_parser_user_question2():
    assert userQuestion.pars == "Openclassrooms"
