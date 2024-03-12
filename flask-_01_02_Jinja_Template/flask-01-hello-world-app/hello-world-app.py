from flask import Flask 
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/second')
def second():
    return "This is the second page"


if __name__ == '__main__':

    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=8081)