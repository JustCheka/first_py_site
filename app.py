from flask import Flask

COUNT = 0

app = Flask(__name__)

@app.route('/test')
def test_function():
    return 'Hello World!'


@app.route('/kek')
def hello_kek():
    return 'hello kek'

@app.route('/counter')
def counter():
    COUNT += 1
    return 'Количество вхождений = ' + str(COUNT)
# if __name__ == '__main__':
#     app.run()