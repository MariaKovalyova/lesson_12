from flask import Flask

from main.blueprints import main_blueprint, load_blueprint  # Импорт блюпринтов

app = Flask(__name__)

app.register_blueprint(main_blueprint)  # Блюпринт главной страницы и поиска поста
app.register_blueprint(load_blueprint)  # Блюпринт добавления нового поста

if __name__ == "__main__":
    """ 127.0.0.1:5000 - дефолтный адрес """
    app.run(debug=True)
