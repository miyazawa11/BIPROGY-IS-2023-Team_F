from flask import Blueprint, request, make_response, jsonify
from attendance.models import child, attendance, teacher
import json

# ルーティング設定
bp = Blueprint("bp", __name__)

@bp.route("/test", methods = ["GET"])
def test():
    return "Hello"
