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
        child_id = request.args.get('child', type=int)
        date = request.args.get('date')

        # 園児のIDと日付がどちらも指定されていない場合はエラーレスポンスを返す
        if child_id is None and date is None:
            return "Error: You should specify either child_id or date", 400

        # 園児のIDしか指定されていない時
        elif date is None:
            attendances = attendance.Attendance.query.filter_by(id_children=child_id).all()
            print(attendances[0].id_children)
            attendance_schema = attendance.Attendance_schema(many=True).dump(attendances)
        
        # 日付しか指定されていない時
        elif child_id is None:
            date_split = date.split('_')
            date_split = [int(date) for date in date_split]
            day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
            attendances = attendance.Attendance.query.filter_by(date=day).all()
            attendance_schema = attendance.Attendance_schema(many=True).dump(attendances)

        else:
            date_split = date.split('_')
            date_split = [int(date) for date in date_split]
            day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
            attendances = attendance.Attendance.query.filter_by(id_children=child_id, date=day).all()
            attendance_schema = attendance.Attendance_schema(many=True).dump(attendances)

        return attendance_schema
    
    if request.method == 'POST':
        payload = request.form

        child_id = payload['id']
        submitted_presence = True if payload['submitted_presence'] == 1 else False
        was_present = True if payload['was_present'] == 1 else False
        reason = payload['reason']
        is_accepted = True if payload['is_accepted'] == 1 else False
        reply_to_reason = payload['reply_to_reason']

        date = payload['date']
        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])

        # すでにその日の出欠が登録されている場合はエラーレスポンスを返す
        existing_attendances = attendance.Attendance.query.filter_by(id_children=child_id, date=day).all()
        if existing_attendances:
            return "Error: This attendance has already reserved", 400

        # 新しい出欠を登録する
        new_attendance = attendance.Attendance(id_children=child_id, submitted_presence=submitted_presence, was_present=was_present, reason=reason, is_accepted=is_accepted, reply_to_reason=reply_to_reason, date=day)

        db.session.add(new_attendance)
        db.session.commit()

        return "OK", 200

    if request.method == 'PUT':
        child_id = request.args.get('child', type=int)
        date = request.args.get('date')

        if child_id is None or date is None:
            return "Error: You should specify both child_id and date", 400

        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
        att = attendance.Attendance.query.filter_by(id_children=child_id, date=day).first()

        if att is None:
            return "Error: This attendance has not reserved yet", 400


        att.is_accepted = not att.is_accepted

        db.session.commit()

        return "OK", 200

