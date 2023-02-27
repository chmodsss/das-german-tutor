from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    image = url_for('static', filename='drjohn.jpg')
    return render_template('index.html', imag=image)

if __name__ == "__main__":
    app.run(debug=True)