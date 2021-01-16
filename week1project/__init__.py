from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myUltraSecretKeyNobodyWillGuess'

from week1project import routes
