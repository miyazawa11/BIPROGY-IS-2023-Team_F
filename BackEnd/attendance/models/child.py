from attendance.database import db
from .attendance import Attendance

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
