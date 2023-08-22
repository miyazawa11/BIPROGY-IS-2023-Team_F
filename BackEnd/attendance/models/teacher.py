from attendance.database import db
from .attendance import Attendance

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
