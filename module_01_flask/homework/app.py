from datetime import datetime, timedelta
from random import choice
from flask import Flask

app = Flask(__name__)
cats = ['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мэйн-Кун', 'Манчкин']
war_words = []


@app.route('/hello_world')
def test_function():
    return 'Привет мир!'


@app.route('/cars')
def test_function1():
    return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def test_function2():
    return choice(cats)


@app.route('/get_time/now')
def test_function3():
    return "Точное время {}".format(datetime.strftime(datetime.now(), '%H.%M.%S'))


@app.route('/get_time/future')
def test_function4():
    return "Точное время через час будет {}".format((datetime.now() + timedelta(hours=1)).time())


@app.route('/get_random_word')
# TODO Обработка файла происходит при каждом вызове эндпоинта.
#  Попробуйте сделать так, чтобы файл разделялся на слова
#  при первом вызове, а результат сохранялся в глобальную
#  переменную. В последующие вызовы, если список слов не
#  пуст, нужно возвращать случайный элемент этого списка.
def test_function5(file_name='war_and_peace.txt'):
    with open(file_name, 'r', encoding='cp1251') as file:
        for line in file:
            for word in line.split():
                war_words.append(word)
    file.close()
    return choice(war_words)
