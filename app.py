import hashlib
import os

from flask import Flask

app = Flask(__name__)


@app.route('/health')
def load_data():

    return 'OK'


@app.route('/orders')
def orders():

    return 'orders will coming !'


if __name__ == '__main__':
    port = os.environ["PORT"]
    print('using port : ', port)
    result = hashlib.md5(b'1585785600597f8475bdfc90d984a3491838c76cd9ff0729f40759496286e09ce81a517e069ebd857f')
    print(result.hexdigest())
    app.run(port=port, host='0.0.0.0')
