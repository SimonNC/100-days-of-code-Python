# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p style="text-align:center">This is a sample web page.</p>' \
           '<p style="text-align:center">This is a paragraph.</p>' \






@app.route("/username/<name>")
def greet(name):
    return f"hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)
