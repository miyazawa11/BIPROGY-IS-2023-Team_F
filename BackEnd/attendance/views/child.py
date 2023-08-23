from flask import Blueprint, request
from attendance.models import child
from attendance.models import attendance
import datetime
child_bp = Blueprint('child', __name__)

@child_bp.route('/reserve', methods=['GET', 'POST', 'PUT'])
def children():

    id_children = request.args.get('id_children')
    date = request.args.get('date')     # YYYY_MM_DDを想定
    
    # YYYY_MM_DD -> YYYY-MM-DDに変換
    date_split = date.split('_')
    date_split = [int(date) for date in date_split]
    day = datetime.date(year=date_split[0], month=date_split[1], day=date_split[2])
    if id_children == None or date == None: return 'error', 400
    
    if request.method == 'POST':
        """
        出欠登録・欠席理由登録
        対象 : 出欠テーブル
        入力 : ユーザー名, 日時, 出欠, 欠席理由
        出力 : ユーザー名, 日時, 出欠, 欠席理由 を入力してレコード追加
        """
        submitted_presence = request.form.get('submitted_presence')
        if submitted_presence == None: return 'error', 400
        reason = request.form.get('reason')

        new_post = attendance.Attendance(id_children,date,submitted_presence,reason)
        attendance.Attendance.add_commit(new_post)
    else:
        # GET, PUTではデータの取得部分は共通
        
        record = attendance.Attendance.query.filter_by(id_children = id_children, date = day)
        # record = attendance.Attendance.query.all()
        # print(record)
        if request.method == 'GET':
            """
            出欠登録の閲覧（返信の閲覧）
            対象：出欠テーブル
            入力：ユーザー名, 日時
            出力：ユーザー名, 日時 を指定してレコード取得
            """
            # 取得したレコードをjson化して返す
            record_json = attendance.AttendanceSchema(many = True).dump(record)
            return record_json
        else:
            """
            (PUT)
            出欠登録・欠席理由の更新
            対象：出欠テーブル
            入力：ユーザー名, 日時
            出力：出欠, 欠席理由 を更新してレコード追加
            """
            # 取得したレコードを更新して追加
            record.submitted_presence = request.form.get('reason')
            attendance.Attendance.commit()