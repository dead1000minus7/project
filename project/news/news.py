from flask import request,render_template, Blueprint


news_bp = Blueprint("news",__name__)

@news_bp.route("/create_news")
def create_news():
    return "123"
    #return render_template("news/index.html")