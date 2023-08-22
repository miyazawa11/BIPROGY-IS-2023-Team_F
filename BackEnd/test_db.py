from attendance.test import app, db, Children, Attendance, Teachers
import datetime


# Create columns
first_name="hoge"
last_name="huge"
kana_last_name="hoge"
kana_first_name="huga"

username = "hogehuga"
created_at = datetime.datetime.now()

is_monday = True
is_tuesday = True
is_wednesday = True
is_thursday = True
is_friday = True
is_saturday = True
is_sunday = True
new_child = Children(first_name=first_name, last_name=last_name, kana_last_name=kana_last_name, kana_first_name=kana_first_name, username=username, created_at=created_at, is_monday=is_monday, is_tuesday=is_tuesday, is_wednesday=is_wednesday, is_thursday=is_thursday, is_friday=is_friday, is_saturday=is_saturday, is_sunday=is_sunday)



username = "hoge"
first_name = "huga"
last_name = "huga"
kana_first_name = "huga"
kana_last_name = "huga"
created_at = datetime.datetime.now()
new_teacher = Teachers(username=username, first_name=first_name, last_name=last_name, kana_first_name=kana_first_name, kana_last_name=kana_last_name, created_at=created_at)

with app.app_context():
    Children.query.delete()
    Attendance.query.delete()
    Teachers.query.delete()
    db.session.commit()


with app.app_context():
    db.session.add(new_child)
    db.session.add(new_teacher)
    db.session.commit()


with app.app_context():
    child = Children.query.first()
    teacher = Teachers.query.first()

id_child = child.id
submitted_presence = True
was_present = True
date= datetime.datetime.now()
reason = "hoge"
is_accepted = True
checked_by = teacher.id
reply_to_reason = "hogehuga"
new_attendance = Attendance(id_children=id_child, date=date, submitted_presence=submitted_presence, was_present=was_present, reason=reason, is_accepted=is_accepted, checked_by=checked_by, reply_to_reason=reply_to_reason)




with app.app_context():
    db.session.add(new_attendance)
    db.session.commit()


# Get columns
with app.app_context():
    child = Children.query.all()[0]
    attendance = Attendance.query.all()[0]
    print(attendance.checked_by)
