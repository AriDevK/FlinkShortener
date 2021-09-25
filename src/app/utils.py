from json import loads
from os import path, listdir
from secrets import token_urlsafe
from random import choice, randint


BASE_DIR = path.abspath(path.dirname(__file__))
STATIC_DIR = path.abspath(path.join(BASE_DIR, 'static'))


def select_anime_girl() -> str:
    PICTURES_DIR = path.join(STATIC_DIR, 'pictures')
    pictures = list(filter(lambda p: p not in ('404.png', '500.jpg'), listdir(PICTURES_DIR)))
    return choice(pictures)


def select_phrase() -> tuple:
    PHRASES_DIR = path.join(STATIC_DIR, 'mock', 'phrases.json')

    with open(PHRASES_DIR, 'r') as json_file:
        json_data = json_file.read()
        phrases = loads(json_data)

    phrases_quantity = len(phrases)
    selection = str(randint(1, phrases_quantity))
    selected_phrase = phrases.get(selection)

    return (selected_phrase.get("author"), selected_phrase.get("phrase"))


def short_link(link: str) -> str:
    return token_urlsafe(10)
