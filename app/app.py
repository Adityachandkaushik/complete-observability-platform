from flask import Flask
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from routes import register_routes
from tracing import init_tracing

app = Flask(__name__)

register_routes(app)
init_tracing(app)


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)