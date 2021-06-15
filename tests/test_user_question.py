from grandPyBotApp.views import user_question
#! /usr/bin/env python3
# coding utf-8

import pytest

from grandPyBotApp.user_question import UserQuestion


userQuestion = UserQuestion("Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?")

def test_form_user_question():
    assert userQuestion.form == "Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?"

def test_parser_user_question():
    assert userQuestion.pars == "Salut GrandPy connais l'adresse d'Openclassrooms"

userQuestion1 = UserQuestion("où est Openclassrooms")

def test_parser_user_question():
    assert userQuestion1.pars == "Openclassrooms"