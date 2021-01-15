from flask import Flask, render_template
import os
from flask_bootstrap import Bootstrap
import process as p


IMAGES_FOLDER = os.path.join('static/images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'droplets.jpg')
    print(full_filename)
    p.example("Welcome")
    return render_template('index.html', user_image=full_filename, time="")


@app.route('/update_results', methods=['POST', 'GET'])
def update_results():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'painting.jpg')
    print(full_filename)

    time_left = p.example("New Image ")

    return render_template('index.html', user_image=full_filename, time=time_left)


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


if __name__ == '__main__':
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True
    app.run(debug=True)
