from collections import Counter
from random import Random
import time

from flask import jsonify
from flask_apispec import use_kwargs
from marshmallow import fields

from app import app, app_docs

random = Random()
requests_per_second_counter = Counter()


@app.route('/api/index', methods=["POST"])
@use_kwargs({
    "name": fields.String(required=True),
    "directory": fields.String(required=True),
    "host": fields.String(required=True),
    "file_size": fields.Int(required=True),
    "permissions": fields.List(fields.Dict())
})
def index(name: str, directory: str, host: str, file_size: int, permissions: dict):
    # Increment the "requests-per-second" pseudo counter
    requests_per_second_counter[int(time.time())] += 1

    # DO some CPU Intensive Task here, takes about 50ms on my laptop
    _ = 100 ** 50000

    return "OK"


@app.route('/api/query/dashboard', methods=["GET"])
def dashboard():
    # ====================================================
    # Calculate the "Stress" on the /api/index endpoint
    # ====================================================
    # use int() to shave the ms from the time()
    now = int(time.time())
    reqs_last_seconds = 0
    for i in range(1, 6):
        reqs_last_seconds += requests_per_second_counter[now - i]
    reqs_last_second = (reqs_last_seconds / 5) * 3
    # Sleep is the stress on the ES server
    time.sleep(0.01 * reqs_last_seconds)

    # DO some CPU Intensive Task here, takes about 50ms on my laptop
    _ = 100 ** 50000

    return jsonify({
        "dasbhoard": {
            "documents": random.randint(0, 100000),
            "persec": reqs_last_second
        }
    })


app_docs.register(index)
app_docs.register(dashboard)
