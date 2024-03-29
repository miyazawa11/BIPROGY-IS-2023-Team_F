from flask import Blueprint, request, jsonify
from attendance.models.attendance import Attendance, AttendanceSchema
from attendance.models.child import Children, ChildrenSchema ,DAYS_OF_WEEK
from attendance.models.teacher import Teachers, TeachersSchema
from attendance.database import db, ma
import datetime
import json
import inspect
from sqlalchemy import select, or_
from sqlalchemy.dialects.sqlite import insert as sqlite_upsert

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher', methods=['GET'])
def teachers():
    teachers = Teachers.query.all()
    teacher_schema = TeachersSchema(many=True).dump(teachers)
    return teacher_schema

@teacher_bp.route('/list',methods=['GET'])
def getlist():
    req = request.args
    if 'date' not in req:
        return "Arg 'date' is missing", 400
    #dateはYYYY-MM-DD YYYY_MM_DD入力を想定
    q_date = datetime.datetime.strptime(req['date'].replace('_','-'),'%Y-%m-%d').date()
    reserved = db.session.execute(\
        select(Attendance.id_children,Attendance.submitted_presence,Attendance.was_present)\
            .filter(Attendance.date == q_date)).all()
    colname="is_"+DAYS_OF_WEEK[q_date.weekday()]
    scheduled = db.session.execute(\
        select(Children.id, Children.first_name, Children.last_name)\
            .filter(getattr(Children,colname) == True)).all()

    ret={}
    for e in scheduled:
        ret[e.id]={
            'id_children':e.id,\
            'first_name':e.first_name,\
            'last_name':e.last_name,\
            'attend':True,\
            'was_present':None
        }
    for e in reserved:
        if e.id_children in ret:
            ret[e.id_children]['attend']=e.submitted_presence
            ret[e.id_children]['was_present']=e.was_present
        else:
            e_dat:Children=db.session.get(Children, e.id_children)
            assert e_dat is not None, "Wrong id_children"
            ret[e.id_children]={\
                'id_children':e.id_children,\
                'first_name':e_dat.first_name,\
                'last_name':e_dat.last_name,\
                'attend':e.submitted_presence,\
                'was_present':e.was_present
            }
    return list(ret.values())

@teacher_bp.route('/list',methods=['POST', 'PUT'])
def update_list():
    #json配列を受け取る [ {'key': val},{'key': val}, ... ]
    req = json.loads(request.data)
    
    for e in req:
        if "id_children" not in e or "was_present" not in e:
            return 'Wrong request', 400
        date=datetime.date.today()
        if "date" in e:
            date = datetime.datetime.strptime(\
                e['date'].replace('_','-'),'%Y-%m-%d').date()
        trg=db.session.execute(select(Attendance)\
            .filter(\
                Attendance.id_children==e['id_children'],\
                Attendance.date==date)).one_or_none()
        if trg is not None:
            trg.Attendance.was_present=e['was_present']
        else:
            record=Attendance(\
                id_children=e['id_children'],
                date=date,
                was_present=e['was_present'])
            db.session.add(record)
    try:
        db.session.flush()
        db.session.rollback()
    except:
        return 'DB Error', 500
    db.session.commit()

    return 'OK',200

@teacher_bp.route('/reserve', methods=['GET', 'POST', 'PUT'])
def reserve():
    if request.method == 'GET':
        id_children = request.args.get('id_children', type=int)
        date = request.args.get('date')

        # 園児のIDと日付がどちらも指定されていない場合はエラーレスポンスを返す
        if id_children is None and date is None:
            return "Error: You should specify either id_children or date", 400

        # 園児のIDしか指定されていない時
        elif date is None:
            attendances = Attendance.query.filter_by(id_children=id_children).all()
            attendance_schema = AttendanceSchema(many=True).dump(attendances)
        
        # 日付しか指定されていない時
        elif id_children is None:
            date_split = date.split('_')
            date_split = [int(date) for date in date_split]
            day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
            attendances = Attendance.query.filter_by(date=day).all()
            attendance_schema = AttendanceSchema(many=True).dump(attendances)

        else:
            date_split = date.split('_')
            date_split = [int(date) for date in date_split]
            day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
            attendances = Attendance.query.filter_by(id_children=id_children, date=day).all()
            attendance_schema = AttendanceSchema(many=True).dump(attendances)
        return attendance_schema
    
    elif request.method == 'POST':
        payload = request.form

        id_children = payload['id_children']
        submitted_presence = payload['submitted_presence']
        if submitted_presence == 'True':
            submitted_presence = True
        elif submitted_presence == 'False':
            submitted_presence = False
        else:
            submitted_presence = None

        was_present = payload['was_present']
        if was_present == 'True':
            was_present = True
        elif was_present == 'False':
            was_present = False
        else:
            was_present = None

        reason = payload['reason']
        is_accepted = True if payload['is_accepted'] == 'True' else False
        reply_to_reason = payload['reply_to_reason']

        date = payload['date']
        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])

        # すでにその日の出欠が登録されている場合はエラーレスポンスを返す
        existing_attendances = Attendance.query.filter_by(id_children=id_children, date=day).all()
        if existing_attendances:
            return "Error: This attendance has already reserved", 400

        # 新しい出欠を登録する
        new_attendance = Attendance(id_children=id_children, submitted_presence=submitted_presence, was_present=was_present, reason=reason, is_accepted=is_accepted, reply_to_reason=reply_to_reason, date=day)

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
        att = Attendance.query.filter_by(id_children=id_children, date=day).first()

        # その日の出欠が登録されていない場合はエラーレスポンスを返す
        if att is None:
            return "Error: This attendance has not reserved yet", 400

        if ('reply_to_reason' in request.form):
            att.reply_to_reason = request.form['reply_to_reason']
        is_accepted = True if request.form['is_accepted'] == 'True' else False

        att.is_accepted = is_accepted

        db.session.commit()

        return "OK", 200
    return "Somthing wrong", 400

@teacher_bp.route('/id',methods=["GET"])
def teacher_id():
    req=request.args
    if 'id' in req:
        trg=db.session.get(Teachers, req['id'])
        if trg is None:
            return "Invalid id", 400
        return trg.username,200
    if 'username' in req:
        trg=db.session.execute(select(Teachers).filter(Teachers.username==req['username'])).one_or_none()
        if trg is None:
            return "Invalid username", 400
        return jsonify(trg.Teachers.id),200
    else:
        return "bad request",400

@teacher_bp.route('/cancel',methods=["GET"])
def cancel_reserve_t():
    req = request.args
    if 'id_children' not in req or 'date' not in req:
        return "bad request",400
    date=datetime.datetime.strptime(req['date'].replace("_","-"),"%Y-%m-%d").date()
    trg=db.session.execute(select(Attendance)\
        .where(Attendance.id_children == req['id_children'],Attendance.date==date)).one_or_none()
    if trg is None:
        return "Invalid record",400
    t=db.session.get(Attendance,trg[0].id)
    print(t)
    db.session.delete(t)
    try:
        db.session.flush()
    except:
        db.session.rollback()
        return "DB Error",500
    db.session.commit()
    return "OK", 200

@teacher_bp.route('/search',methods=["GET"])
def search_children():
    req = request.args
    if 'name' not in req and 'date' not in req and 'dow' not in req:
        ret = db.session.execute(select(Children)).all()
        return ChildrenSchema(many=True).dump([ e[0] for e in ret ]), 200
    stmt=select(Children)
    idlist=set()
    datesearch=False
    q_date=None
    
    if 'date' in req:
        datesearch=True
        q_date=datetime.datetime.strptime(req['date'].replace("_","-"),"%Y-%m-%d").date()
        candidate_dt=db.session.execute(select(Attendance.id_children)\
            .where(Attendance.date==q_date)).all()
        for e in candidate_dt:
            idlist.add(e[0])

    if 'dow' in req or 'date' in req:
        datesearch=True
        if 'dow' not in req:
            assert q_date
            dow=q_date.weekday()
        else:
            dow=int(req['dow'])
        if q_date is not None and (dow!=q_date.weekday()):
            return jsonify([]),200
        colname="is_"+DAYS_OF_WEEK[dow]
        candidate_dw=db.session.execute(select(Children.id)\
            .filter(getattr(Children,colname) == True)).all()
        for e in candidate_dw:
            idlist.add(e[0])
    print("!")
    print(idlist)
    idlist=list(idlist)
    if datesearch and (not idlist):
        return jsonify([]),200
    else:
        stmt=stmt.filter(Children.id.in_(idlist))
    
    if 'name' in req:
        q_name=req['name']
        stmt=stmt.filter(or_(\
            Children.first_name.contains(q_name),
            Children.last_name.contains(q_name),
            Children.kana_first_name.contains(q_name),
            Children.kana_last_name.contains(q_name),
            (Children.last_name+Children.last_name).contains(q_name),
            (Children.kana_last_name+Children.kana_last_name).contains(q_name)
        ))
    print(idlist)
    result=db.session.execute(stmt).all()
    ret=[ e[0] for e in result ]
    print(ChildrenSchema(many=True).dump(ret))
    return ChildrenSchema(many=True).dump(ret), 200
