from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import create_access_token, JWTManager, jwt_required
from decouple import config, Config


app = Flask(__name__)
app.config["DEBUG"] = True
swagger = Swagger(app)
app.config["JWT_SECRET_KEY"] = 'secret'
jwt = JWTManager(app)
