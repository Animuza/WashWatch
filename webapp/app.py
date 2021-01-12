from flask import Flask, render_template
import os

IMAGES_FOLDER = os.path.join('static/images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

@app.route('/')
def index():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'droplets.jpg')
	print(full_filename)
	return render_template('index.html', user_image = full_filename)

@app.route('/cakes')
def cakes():
	return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
