from flask import Flask

app = Flask(__name__)


@app.route('/')
def blabla():
    return "Hello world from Sivasurya"

if __name__ == "__main__":
    app.run(debug=True)