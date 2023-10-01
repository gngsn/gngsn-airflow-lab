import json
from datetime import datetime

from flask import Flask

app = Flask(__name__)

response = {"date": datetime.now(), "user": "sun"}


@app.route('/events')
def hello():
    return json.dumps(response, indent=4, sort_keys=True, default=str)

# flask run
