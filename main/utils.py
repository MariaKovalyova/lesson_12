import json
import logging
from json import load  # Импорт билиотеки для загрузки файла
from config import ALLOWED_EXTENSIONS

def load_post_from_sjson(path):  # Функция загрузки файла с постами
    """ Обработка ошибки, если файл не открывается или не существует"""
    try:
        with open(path, 'r', encoding="UTF=8") as file:
            return load(file)
    except (FileNotFoundError, FileExistsError):
        logging.ERROR("The json file can't be opened or doesn't exist")
        return "The json file can't be opened or doesn't exist"


def get_post_with_word(posts_path, word):

    post_list = []  # список подходящих кандидатов
    posts = load_post_from_sjson(posts_path)

    for post in posts:  # Отправляем ссылку на json в функцию для загрузки
        if word.lower() in (post.get('content')).lower().split():
            post_list.append(post)

    return post_list


def add_new_post(path, new_content, new_picture):  # Функция добавления нового файла
    data = load_post_from_sjson(path)
    data.append({"pic": new_picture, "content": new_content})
    with open(path, 'w') as file:
        json.dump(data, file)


def allowed_file(filename):  # Функция проверки расширения файла
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
