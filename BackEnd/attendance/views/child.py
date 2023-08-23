from flask import Blueprint, request
from attendance.models import child

child_bp = Blueprint('child', __name__)

@child_bp.route('/children', methods=['GET'])
def children():
    if request.method == 'GET':
        children = child.Children.query.all()
        children_schema = child.ChildrenSchema(many=True).dump(children)
        return children_schema
