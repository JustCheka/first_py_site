from flask import Flask


app = Flask(__name__)

@app.route('/test')
def test_function():
    return 'Hello World!'


@app.route('/kek')
def hello_kek():
    return 'hello kek'
# if __name__ == '__main__':
#     app.run()