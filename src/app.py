from flask import Flask
from routes.contacs import contacts

app = Flask(__name__)

app.register_blueprint(contacts)



