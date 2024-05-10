from flask import Flask

app = Flask(__name__)


@app.route('/')
@make_bold

def hello_world():
    return '<h1 style="text-align: center">Welcome</h1>' \
           '<p style="text-align: center">This is my first website that im creating</p>'


@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)