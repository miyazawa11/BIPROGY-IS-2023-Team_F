from flask import Flask, make_response, jsonify

from .views.child import child_bp
from .views.teacher import teacher_bp
from attendance.database import db  # dbインスタンス(appとの紐づけ前)
import config                       # 設定ファイル(文字列の形で読み込むのでVScodeだとnot accessed)

# from flask_cors import CORS

def create_app():
    """
    appインスタンス作成
    """

    # appインスタンス作成
    app = Flask(__name__)

    # CORS対応
    # CORS(app)

    # DB設定を読み込む
    app.config.from_object('config.Config')
    db.init_app(app)

    # routingと処理内容を記述したスクリプトを登録
    app.register_blueprint(child_bp, url_prefix='/api/children/')
    app.register_blueprint(teacher_bp, url_prefix='/api/teacher/')

    return app

# app = create_app()
