from flask import Flask
from routes import routes
from flask_session import Session
import os

app = Flask(__name__)
app.register_blueprint(routes)
SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


if __name__ == '__main__':
  app.debug = True
  app.run(threaded=True,host="0.0.0.0",port=50000)