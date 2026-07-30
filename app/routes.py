import random
import time

from flask import jsonify

from logging_config import logger
from metrics import REQUEST_COUNT, REQUEST_LATENCY


def register_routes(app):

    @app.route("/")
    def home():
        REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

        with REQUEST_LATENCY.labels("/").time():
            logger.info("Home endpoint accessed")

            return jsonify({
                "message": "Complete Observability Platform",
                "status": "Running"
            })


    @app.route("/health")
    def health():

        REQUEST_COUNT.labels(method="GET", endpoint="/health").inc()

        with REQUEST_LATENCY.labels("/health").time():

            logger.info("Health Check")

            return jsonify({
                "status": "Healthy"
            })


    @app.route("/users")
    def users():

        REQUEST_COUNT.labels(method="GET", endpoint="/users").inc()

        with REQUEST_LATENCY.labels("/users").time():

            logger.info("Fetching Users")

            users = [
                {"id": 1, "name": "Aditya"},
                {"id": 2, "name": "Sakshi"},
                {"id": 3, "name": "DevOps User"}
            ]

            return jsonify(users)


    @app.route("/kr")
    def kr():

        REQUEST_COUNT.labels(method="GET", endpoint="/kr").inc()

        with REQUEST_LATENCY.labels("/kr").time():

            logger.info("KR endpoint accessed")

            return jsonify({
                "message": "KR endpoint active",
                "status": "OK"
            })


    @app.route("/login")
    def login():

        REQUEST_COUNT.labels(method="GET", endpoint="/login").inc()

        with REQUEST_LATENCY.labels("/login").time():

            delay = random.uniform(0.2, 1.5)

            time.sleep(delay)

            logger.info(f"User Login Successful | Response Time {delay:.2f} sec")

            return jsonify({
                "message": "Login Successful",
                "response_time": round(delay, 2)
            })


    @app.route("/error")
    def error():

        REQUEST_COUNT.labels(method="GET", endpoint="/error").inc()

        logger.error("Dummy Error Generated")

        return jsonify({
            "error": "Something went wrong"
        }), 500