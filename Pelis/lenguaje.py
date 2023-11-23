from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Pelis.db import get_db

bp = Blueprint('language', __name__,url_prefix="/language/")

@bp.route('/')
def index():
    db = get_db()
    language = db.execute(
        """SELECT name  FROM language """
    ).fetchall()
    return render_template('lenguaje/index.html', language= language)