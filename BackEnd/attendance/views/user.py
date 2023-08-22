from flask import Blueprint, request, make_response, jsonify, render_template
from attendance.models import child, attendance, teacher
import json

# ルーティング設定
bp = Blueprint("bp", __name__)

@bp.route("/test1", methods = ["GET"])
def test():
    return "Hello"
@bp.route("/test2", methods = ["GET","POST"])
def showdb():
    if request.method == "GET":
        posts = child.Children().query.all()
        print(type(posts[0]))
        print(posts)
        # return render_template("test2.html", posts=posts)
        return child.ChildrenSchema(many = True).dump(posts)