from attendance import app, db
from attendance.models.child import Children
from attendance.models.teacher import Teachers
from attendance.models.attendance import Attendance
import datetime
from datetime import timedelta
from dummy_data import CHILDREN, TEACHERS

def clear_db():
    with app.app_context():
        Children.query.delete()
        Attendance.query.delete()
        Teachers.query.delete()
        db.session.commit()

def create_child():
    for child in CHILDREN:
        username = child["username"]
        first_name = child["first_name"]
        last_name = child["last_name"]
        kana_first_name = child["kana_first_name"]
        kana_last_name = child["kana_last_name"]
        is_sunday = child["is_sunday"]
        is_monday = child["is_monday"]
        is_tuesday = child["is_tuesday"]
        is_wednesday = child["is_wednesday"]
        is_thursday = child["is_thursday"]
        is_friday = child["is_friday"]
        is_saturday = child["is_saturday"]
        created_at = datetime.datetime.now()

        new_child = Children(username=username, first_name=first_name, last_name=last_name, kana_first_name=kana_first_name, kana_last_name=kana_last_name, is_sunday=is_sunday, is_monday=is_monday, is_tuesday=is_tuesday, is_wednesday=is_wednesday, is_thursday=is_thursday, is_friday=is_friday, is_saturday=is_saturday, created_at=created_at)


        with app.app_context():
            db.session.add(new_child)
            db.session.commit()

    print("Children created")


def create_teacher():
    for teacher in TEACHERS:
        username = teacher["username"]
        first_name = teacher["first_name"]
        last_name = teacher["last_name"]
        kana_first_name = teacher["kana_first_name"]
        kana_last_name = teacher["kana_last_name"]
        created_at = datetime.datetime.now()
        new_teacher = Teachers(username=username, first_name=first_name, last_name=last_name, kana_first_name=kana_first_name, kana_last_name=kana_last_name, created_at=created_at)

        with app.app_context():
            db.session.add(new_teacher)
            db.session.commit()

    print("Teachers created")

def create_attendance():

    with app.app_context():
        children = Children.query.all()
        teacher = Teachers.query.all()[0]
    
    # 園児ごとに過去2週間分のダミーデータを作成
    for child in children:

        for i in range(1, 15):
            id_child = child.id
            if i % 2 == 0:
                submitted_presence = True
            else:
                submitted_presence = False
            was_present = None
            date= datetime.date.today()-timedelta(days=i)
            reason = "今日も元気です。"
            is_accepted = False
            checked_by = teacher.id
            reply_to_reason = ""
            new_attendance = Attendance(id_children=id_child, date=date, submitted_presence=submitted_presence, was_present=was_present, reason=reason, is_accepted=is_accepted, checked_by=checked_by, reply_to_reason=reply_to_reason)

            with app.app_context():
                db.session.add(new_attendance)
                db.session.commit()

    print("Attendance created")



#generate_data()
clear_db()
create_child()
create_teacher()
create_attendance()
