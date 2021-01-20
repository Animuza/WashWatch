
from random import seed
from random import randint, random

from flask import request, jsonify

from app import PushSubscription
from webpush_handler import trigger_push_notifications_for_subscriptions

minutes = 0


def trigger_push_notifications():
    json_data = request.get_json()
    subscriptions = PushSubscription.query.all()
    results = trigger_push_notifications_for_subscriptions(
        subscriptions,
        'WashApp here!', 'The washing machine is ready!'
    )
    return jsonify({
        "status": "success",
        "result": results
    })


def example(test):
    global minutes

    print(test)
    # seed random number generator
    seed(345)
    # generate some random numbers
    hours = randint(0, 4)
    minutes += 1
    if minutes % 4 == 0:
        trigger_push_notifications()

    print("Time left: " + str(hours) + ":" + str(minutes))
    return str(hours) + ":" + str(minutes)
