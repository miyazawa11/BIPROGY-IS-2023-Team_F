from flask import Blueprint, request
from attendance.database import db
from attendance.models import teacher
from attendance.models import attendance
import datetime

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher', methods=['GET'])
def teachers():
    if request.method == 'GET':
        teachers = teacher.Teachers.query.all()
        teacher_schema = teacher.TeachersSchema(many=True).dump(teachers)
        return teacher_schema

@teacher_bp.route('/reserve', methods=['GET', 'POST', 'PUT'])
def reserve():
    if request.method == 'GET':
        id_children = request.args.get('id_childlen', type=int)
        date = request.args.get('date')

        # 園児のIDと日付がどちらも指定されていない場合はエラーレスポンスを返す
        if id_children is None and date is None:
            return "Error: You should specify either id_children or date", 400

        # 園児のIDしか指定されていない時
        elif date is None:
            attendances = attendance.Attendance.query.filter_by(id_children=id_children).all()
            attendance_schema = attendance.AttendanceSchema(many=True).dump(attendances)
        
        # 日付しか指定されていない時
        elif id_children is None:
            date_split = date.split('_')
            date_split = [int(date) for date in date_split]
            day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
            attendances = attendance.Attendance.query.filter_by(date=day).all()
            attendance_schema = attendance.AttendanceSchema(many=True).dump(attendances)

        else:
            date_split = date.split('_')
            date_split = [int(date) for date in date_split]
            day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
            attendances = attendance.Attendance.query.filter_by(id_children=id_children, date=day).all()
            attendance_schema = attendance.AttendanceSchema(many=True).dump(attendances)

        return attendance_schema
    
    elif request.method == 'POST':
        payload = request.form

        id_children = payload['id_children']
        submitted_presence = True if payload['submitted_presence'] == 'True' else False
        was_present = True if payload['was_present'] == 'True' else False
        reason = payload['reason']
        is_accepted = True if payload['is_accepted'] == 'True' else False
        reply_to_reason = payload['reply_to_reason']

        date = payload['date']
        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])

        # すでにその日の出欠が登録されている場合はエラーレスポンスを返す
        existing_attendances = attendance.Attendance.query.filter_by(id_children=id_children, date=day).all()
        if existing_attendances:
            return "Error: This attendance has already reserved", 400

        # 新しい出欠を登録する
        new_attendance = attendance.Attendance(id_children=id_children, submitted_presence=submitted_presence, was_present=was_present, reason=reason, is_accepted=is_accepted, reply_to_reason=reply_to_reason, date=day)

        db.session.add(new_attendance)
        db.session.commit()

        return "OK", 200

    elif request.method == 'PUT':
        id_children = request.form['id_children']
        date = request.form['date']

        # 園児のIDと日付がどちらも指定されていない場合はエラーレスポンスを返す
        if id_children is None or date is None:
            return "Error: You should specify both id_children and date", 400

        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
        att = attendance.Attendance.query.filter_by(id_children=id_children, date=day).first()

        # その日の出欠が登録されていない場合はエラーレスポンスを返す
        if att is None:
            return "Error: This attendance has not reserved yet", 400

        if ('reply_to_reason' in request.form):
            att.reply_to_reason = request.form['reply_to_reason']
        is_accepted = True if request.form['is_accepted'] == 'True' else False

        att.is_accepted = is_accepted

        db.session.commit()

        return "OK", 200

