from flask import Blueprint, request, jsonify
from attendance.models import child
from attendance.models.child import Children
from attendance.models import attendance
from attendance.models.attendance import Attendance, AttendanceSchema
from attendance.database import db
from sqlalchemy import select, delete
import datetime
child_bp = Blueprint('child', __name__)

def ch_id_to_name(id):
    trg=db.session.get(child.Children, id)
    if trg is None:
        return ""
    return trg.username
def ch_name_to_id(name):
    trg=db.session.execute(select(child.Children).filter(child.Children.username==name)).one_or_none()
    if trg is None:
        return -1
    return trg.Children.id

@child_bp.route('/reserve', methods=['GET', 'POST', 'PUT'])
def children():


    if request.method == 'POST':
        """
        出欠登録・欠席理由登録
        対象 : 出欠テーブル
        入力 : ユーザー名, 日時, 出欠, 欠席理由
        出力 : ユーザー名, 日時, 出欠, 欠席理由 を入力してレコード追加
        """

        # フォームの内容を取得
        submitted_presence = request.form.get('submitted_presence')
        if submitted_presence == 'True':
            submitted_presence = True
        elif submitted_presence == 'False':
            submitted_presence = False
        else:
            submitted_presence = None

        reason = request.form.get('reason')
        id_children = request.form.get('id_children')
        date = request.form.get('date')     # YYYY_MM_DDを想定
        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
        
        existing_attendances = attendance.Attendance.query.filter_by(id_children=id_children, date=day).all()
        if existing_attendances:
            return "Error: This attendance has already reserved", 400

        # 新規レコード作成(フォーム以外の項目の内容を作成)
        new_post = attendance.Attendance(
            id_children = id_children,
            date = day,
            submitted_presence = submitted_presence,
            reason = reason,
            is_accepted = False,
            was_present = None,
            checked_by = None,
            reply_to_reason = None
        )
        attendance.Attendance.add_commit(new_post)
        return "OK", 200

    elif request.method == 'GET':
        """
        出欠登録の閲覧（返信の閲覧）
        対象：出欠テーブル
        入力：ユーザー名, 日時
        出力：ユーザー名, 日時 を指定してレコード取得
        """

        # GETパラメータの取得
        id_children = request.args.get('id_children')
        date = request.args.get('date')     # YYYY_MM_DDを想定
        # YYYY_MM_DD -> YYYY-MM-DDに変換
        if id_children == None or date == None:
            return 'Error: You shold specify both id_children and date to register attendance.', 400

        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])

        # GET, PUTでデータの取得部分は共通
        record = attendance.Attendance.query.filter_by(id_children = id_children, date = day)


        # 取得したレコードをjson化して返す
        record_json = attendance.AttendanceSchema(many = True).dump(record)
        return record_json
    elif request.method == 'PUT':
        """
        (PUT)
        出欠登録・欠席理由の更新
        対象：出欠テーブル
        入力：ユーザー名, 日時
        出力：出欠, 欠席理由 を更新してレコード追加
        """

        id_children = request.form.get('id_children')
        date = request.form.get('date')     # YYYY_MM_DDを想定
        date_split = date.split('_')
        date_split = [int(date) for date in date_split]
        day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
        
        record = attendance.Attendance.query.filter_by(id_children = id_children, date = day).first()
        if not record:
            return "Error: This attendance has not reserved yet", 400

        # 編集後の内容を取得
        submitted_presence = request.form.get('submitted_presence')
        reason = request.form.get('reason')
        if submitted_presence == 'True':
            submitted_presence = True
        elif submitted_presence == 'False':
            submitted_presence = False
        else:
            submitted_presence = None

        # 取得したレコードを更新して追加           
        record.submitted_presence = submitted_presence
        record.reason = reason
        attendance.Attendance.commit()
        return "OK", 200

@child_bp.route('/id',methods=["GET"])
def child_id():
    req=request.args
    if 'id' in req:
        ret=ch_id_to_name(req['id'])
        if ret=="":
            return "Invalid ID", 400
        return ret,200
    if 'username' in req:
        ret=ch_name_to_id(req['username'])
        if ret == -1:
            return "Invalid username", 400
        return jsonify(ret),200
    else:
        return "bad request",400

@child_bp.route('/cancel',methods=["GET"])
def cancel_reserve_c():
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
@child_bp.route('/history',methods=["GET"])
def child_history():
    req=request.args
    id=-1
    if 'id' in req:
        trg=db.session.get(child.Children, req['id'])
        if trg is None:
            return "Invalid ID", 400
        id=req['id']
    if 'username' in req:
        ret=ch_name_to_id(req['username'])
        if ret == -1:
            return "Invalid username", 400
        id=ret
    assert id != -1
    print(id)
    result=db.session.execute(\
        select(Attendance).filter(Attendance.id_children==id)).all()
    result_list=[ e[0] for e in result ]
    print(result)
    return AttendanceSchema(many=True).dump(result_list), 200
