from flask import Blueprint, request
from attendance.models import teacher

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher', methods=['GET'])
def teachers():
    if request.method == 'GET':
        teachers = teacher.Teachers.query.all()
        teacher_schema = teacher.TeachersSchema(many=True).dump(teachers)
        return teacher_schema
