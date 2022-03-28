"""
Давайте немного вспомним Linux command line утилиты.

Напишите Flask GET endpoint, который на вход принимает флаги командной строки,
    а возвращает результат запуска команды PS с этими флагами.
    Чтобы красиво отформатировать результат вызова программы - заключите его в тэг <pre>:
        <pre>Put your text here</pre>

Endpoint должен быть по url = /ps и принимать входные значение через аргумент arg
Напомню, вызвать программу ps можно, например, вот так

    >>> import shlex, subprocess
    >>> command_str = f"ps aux"
    >>> command = shlex.split(command_str)
    >>> result = subprocess.run(command, capture_output=True)
"""


import shlex
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def _ps():
    prefix_list = request.args.getlist('arg')
    command_str = f"ps {' '.join(prefix_list)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True, encoding='utf-8').stdout
    return f'<pre>{result}</pre>'


if __name__ == "__main__":
    app.run(debug=True)
