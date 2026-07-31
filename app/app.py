from flask import Flask
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from logging_config import logger
from routes import register_routes
from tracing import init_tracing


def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    register_routes(app)
    init_tracing(app)

    @app.route("/metrics")
    def metrics():
        logger.info("Metrics endpoint initialized at /metrics")
        return generate_latest(), 200, {
            "Content-Type": CONTENT_TYPE_LATEST
        }

    return app


app = create_app()


if __name__ == "__main__":
    logger.info("Starting Flask application on port 5000")
    app.run(host="0.0.0.0", port=5000, debug=True)