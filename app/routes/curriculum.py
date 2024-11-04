from flask import Blueprint, render_template

bp_curriculum = Blueprint("main", __name__)


@bp_curriculum.route("/", methods=["GET"])
def send_curriculum():
    return render_template("curriculum.html")
