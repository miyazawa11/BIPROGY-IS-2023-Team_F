from flask import Blueprint, request, jsonify
from attendance.models.attendance import Attendance, AttendanceSchema
from attendance.models.child import Children, ChildrenSchema ,DAYS_OF_WEEK
from attendance.models.teacher import Teachers, TeachersSchema
from attendance.database import db, ma
import datetime
import json
import pprint
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher', methods=['GET'])
def teachers():
    teachers = Teachers.query.all()
    teacher_schema = TeachersSchema(many=True).dump(teachers)
    return teacher_schema

@teacher_bp.route('/list',methods=['GET'])
def getlist():
    req = request.args
    q_date = datetime.datetime.strptime(req['date'],'%Y-%m-%d').date()
    reserved = db.session.execute(\
        db.select(Attendance.id_children,Attendance.submitted_presence)\
            .filter(Attendance.date == q_date)).all()
    colname="is_"+DAYS_OF_WEEK[q_date.weekday()]
    scheduled = db.session.execute(\
        db.select(Children.id, Children.first_name, Children.last_name)\
            .filter(getattr(Children,colname) == True)).all()

    ret={}
    for e in scheduled:
        ret[e.id]={
            'id_children':e.id,\
            'first_name':e.first_name,\
            'last_name':e.last_name,\
            'attend':True\
        }
    for e in reserved:
        if e.id_children in ret:
            ret[e.id_children]['attend']=e.submitted_presence
        else:
            e_dat=db.session.get(Children, e.id_children)
            ret[e.id_children]={\
                'id_children':e.id_children,\
                'first_name':e_dat.first_name,\
                'last_name':e_dat.last_name,\
                'attend':e.submitted_presence
            }
    return json.dumps(list(ret.values()))

@teacher_bp.route('/', methods=['GET'])
def root():
    return "root"