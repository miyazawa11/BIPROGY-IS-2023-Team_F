from flask import Flask, make_response, jsonify
# from flask_cors import CORS
from attendance.database import db
import config

def create_app():

  app = Flask(__name__)

  # CORS対応
  # CORS(app)

  # DB設定を読み込む
  app.config.from_object('config.Config')
  db.init_app(app)

  return app

app = create_app()
