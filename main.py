from flask import Flask, request, render_template
from flask_restful import Api, Resource

from hashlib import md5
import os
import requests

from app.config import app
from app.models import User
from app.database import db


api = Api(app)

class LoginEndpoint(Resource):
    def get(self):
        return "allowed methods: [POST]"

    def post(self):
        try:
            username = request.json.get("username").strip()
            password = md5((request.json.get("password").strip()).encode()).hexdigest()

        except Exception as e:
            print(str(e))

            return "user credentials not found"

        user = User.query.filter_by(username=username, password=password).first()
        if user is not None:
            return "login successful"
        else:
            return "invalid login credentials"


class RegisterEndpoint(Resource):
    def get(self):
        return "allowed methods: [POST]"

    def post(self):
        try: 
            username = request.json.get("username").strip()
            email = request.json.get("email").strip()
            password = request.json.get("password").strip()

        except Exception as e:
            print(str(e))

            return "failed to retrieve credentials"

        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.password = md5(password.encode()).hexdigest()

        db.session.add(new_user)
        db.session.commit()
    
        return "registration successful"


api.add_resource(LoginEndpoint, "/api/login")
api.add_resource(RegisterEndpoint, "/api/register")


if __name__ == "__main__":
    app.run(debug=True)

