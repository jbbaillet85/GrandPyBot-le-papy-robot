from stop_word import list_words

def get_user_question(data):
    """[method retrieving the user's question ]
    Args:
        data ([string]): [user_question]
    Returns:
        [string]: [user_question]
    """
    return data

def parser_user_question(requete):
    """[method allowing to find the key words in character string]
    Args:
        requete ([string]): [user_question]
    Returns:
        [list]: [keysWords]
    """
    for stopWord in list_words:
        print(stopWord)
        parser = requete.replace(stopWord, " ")
        parser = requete.splite()
    return parser


if __name__ == "main":
    parser1 = parser_user_question("Salut GrandPy! Est-ce que tu connais l'adresse d'Openclassrooms?")
    print(parser1)