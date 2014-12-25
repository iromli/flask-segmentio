from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from flask import Flask
from flask_segmentio import SegmentIO

SEGMENTIO_WRITE_KEY = os.environ.get("SEGMENTIO_WRITE_KEY", "")

app = Flask(__name__)
app.config.from_object(__name__)

analytics = SegmentIO()
analytics.init_app(app)


@app.route("/")
def index():
    analytics.track(
        "johndoe",
        "Posted a blog",
        {
            "title": "hello world",
            "content": "this is a test",
        })
    return "<h1>SENT</h1>"


if __name__ == "__main__":
    app.run(debug=True)
