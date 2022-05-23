import logging  # Импортируем класс для логгирования

from flask import render_template, Blueprint, request
from werkzeug.utils import secure_filename  # Функция проверки файла

from config import POST_PATH, UPLOAD_FOLDER_IMG  # Импорт путей с файлами
from main.utils import *

logging.basicConfig(filename="logger.log", level=logging.INFO, encoding="UTF-8")  # Установка файла для логирования

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")  # Блупринт для главной страницы
load_blueprint = Blueprint("load_blueprint", __name__, template_folder="templates")  # Блупринт для добавления поста

""" Главная страница """
@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")

""" Cтраница Поиска"""
@main_blueprint.route("/search")
def search_page():
    logging.info("Открытие страницы /search")
    s = request.args.get('s', "")  # Получение ?s= аргумента из адресной строки
    posts = get_post_with_word(POST_PATH, s)
    return render_template("post_by_tag.html", s=s, posts=posts)

""" Cтраница добавления поста"""
@load_blueprint.route("/post", methods=["GET"])
def load_post_page():
    logging.info("Открытие страницы /post")
    return render_template("post_form.html")


""" Cтраница добавления поста"""
@load_blueprint.route("/post", methods=["POST"])
def create_new_post_page():

    pic = request.files.get("picture")
    content = request.form.get("content")

    if pic and allowed_file(pic.filename):  # Если файл существует и его расширение подходит нам

        filename = secure_filename(pic.filename)  # Производим проверку файла импортированной функцией
        picture_path = f"{UPLOAD_FOLDER_IMG}/{filename}"
        pic.save(picture_path)  # Сохранение картинки в папку uploads

        logging.info("Файл загружен")

        add_new_post(POST_PATH, content, picture_path) # Функция добавления нового поста

        return render_template("post_uploaded.html", content=content, picture=picture_path)

    else:
        logging.info("Файл не был загружен - недопустимое расширение или файла нет")
        return "Данные отсутствуют или повреждены"
