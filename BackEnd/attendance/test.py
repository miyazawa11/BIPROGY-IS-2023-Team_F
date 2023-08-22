# SQL_Alchemyデータベース定義
# MiroのER図参照

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///attendance.db"
db = SQLAlchemy(app)

DAYS_OF_WEEK = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

class Children(db.Model):
    __tablename__ = "children_table"
    """
    園児用テーブル
    """
    # 主キー
    id = db.Column(db.Integer, primary_key = True)

    # 氏名関連
    first_name = db.Column(db.String(10), nullable = False)
    last_name = db.Column(db.String(10), nullable = False)
    kana_first_name = db.Column(db.String(10), nullable = False)
    kana_last_name = db.Column(db.String(10), nullable = False)

    # ユーザーネーム
    username = db.Column(db.String(30), nullable = False, unique = True)

    # レコード作成日時
    created_at = db.Column(db.DateTime, nullable = False)

    # その曜日に園児を預かるかのフラグ(is_monday, is_tuesday, ...)
    for day in DAYS_OF_WEEK:
        exec("is_" + day + "= db.Column(db.Boolean, nullable= False)")

    # 各曜日で園児を預かる時間
    for day in DAYS_OF_WEEK:
        exec("coming_time_" + day + "= db.Column(db.Time, nullable = True)")
        exec("go_home_time_" + day + "= db.Column(db.Time, nullable = True)")

    # FK親側(db.relationship(クラス名, backref=""))
    attendance = db.relationship("Attendance")


class Attendance(db.Model):
    """
    出欠情報テーブル
    """
    __tablename__ = "attendance_table"
    id = db.Column(db.Integer, primary_key = True)
    id_children = db.Column(db.Integer, db.ForeignKey("children_table.id"))    # FK子側
    submitted_presence = db.Column(db.Boolean, nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    was_present = db.Column(db.Boolean, nullable = False)
    reason = db.Column(db.String(500), nullable = True)
    is_accepted = db.Column(db.Boolean, nullable = False)
    checked_by = db.Column(db.Integer, db.ForeignKey("teachers_table.id"))  # FK子側
    reply_to_reason =db.Column(db.String(500), nullable = True)

class Teachers(db.Model):
    """
    保育士テーブル
    """
    __tablename__ = "teachers_table"
    id = db.Column(db.Integer, primary_key = True)  #FK親側
    attendace = db.relationship("Attendance")
    username = db.Column(db.String(30), nullable = False, unique = True)

    # 氏名関連
    first_name = db.Column(db.String(10), nullable = False)
    last_name = db.Column(db.String(10), nullable = False)
    kana_first_name = db.Column(db.String(10), nullable = False)
    kana_last_name = db.Column(db.String(10), nullable = False)

    # レコード作成日時
    created_at = db.Column(db.DateTime, nullable = False)

