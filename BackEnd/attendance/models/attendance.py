from attendance.database import db, ma

class Attendance(db.Model):
    """
    出欠情報テーブル
    """
    __tablename__ = "attendance_table"
    id = db.Column(db.Integer, primary_key = True)
    id_children = db.Column(db.Integer, db.ForeignKey("children_table.id"))    # FK子側
    submitted_presence = db.Column(db.Boolean, nullable = False)
    date = db.Column(db.Date, nullable = False)
    was_present = db.Column(db.Boolean, nullable = False)
    reason = db.Column(db.String(500), nullable = True)
    is_accepted = db.Column(db.Boolean, nullable = False)
    checked_by = db.Column(db.Integer, db.ForeignKey("teachers_table.id"))  # FK子側
    reply_to_reason =db.Column(db.String(500), nullable = True)

<<<<<<< HEAD
class Attendance_schema(ma.SQLAlchemyAutoSchema):
=======
    def commit():
        db.session.commit()

    def add_commit(record):
        db.session.add(record)
        db.session.commit()
    
    def delete_commit(record):
        db.session.delete(record)
        db.session.commit()


class AttendanceSchema(ma.SQLAlchemyAutoSchema):
>>>>>>> develop
    class Meta:
        model = Attendance
