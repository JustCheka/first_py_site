from flask import Flask

count = 0

app = Flask(__name__)



@app.route('/test')
def test_function():
    return 'Hello World!'


@app.route('/kek')
def hello_kek():
    return 'hello kek'

@app.route('/counter')
def counter():
    return 'Количество вхождений = ' + plusCount()


def plusCount():
    global count
    count += 1
    print(count)
    return str(count)

# if __name__ == '__main__':
#     app.run()