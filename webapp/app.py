
import os
import process as p
import GetTime as time
import takePic as pic
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

cwd = os.getcwd()

IMAGES_FOLDER = os.path.join(cwd, 'files')
IMAGES_READ_FOLDER = os.path.join(cwd, 'files/picture.jpeg')
OUTPUT_FOLDER = os.path.join(cwd, 'files/output.txt')

app = Flask(__name__, instance_relative_config=True)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
app.config.from_pyfile('application.cfg.py')

db = SQLAlchemy(app)


class PushSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subscription_json = db.Column(db.Text, nullable=False)


db.create_all()
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER


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
    #The next line needs to be uncommented, when a camera is adapted!
    #pic.takePicture()
    
    time_left = time.getTime()  

    return render_template('index.html', user_image=full_filename, time=time_left)

@app.route('/see_pic', methods=['POST', 'GET'])
def see_pic():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'picture.jpeg')
    print(full_filename)
    #The next line needs to be uncommented, when a camera is adapted!
    #pic.takePicture()
    
    time_left = time.getTime()    

    return render_template('index.html', user_image=full_filename, time=time_left)

@app.route("/api/push-subscriptions", methods=["POST"])
def create_push_subscription():
    json_data = request.get_json()
    subscription = PushSubscription.query.filter_by(
        subscription_json=json_data['subscription_json']
    ).first()
    if subscription is None:
        subscription = PushSubscription(
            subscription_json=json_data['subscription_json']
        )
        db.session.add(subscription)
        db.session.commit()
    return jsonify({
        "status": "success",
        "result": {
            "id": subscription.id,
            "subscription_json": subscription.subscription_json
        }
    })


if __name__ == '__main__':
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True
    #app.run(debug=True, host='0.0.0.0', ssl_context='adhoc')
    app.run(debug=True, host='0.0.0.0')
    #app.config['SERVER_NAME']='washapp:5000'
    