import datetime
from flask import Flask

app = Flask(__name__)
x = 0


@app.route('/test')
def test_function():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


@app.route('/hello/world')
def test_function1():
    return 'hello world'


@app.route('/counter')
def test_function2():
    global x
    x += 1
    return str(x)
