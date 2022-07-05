from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

from project.news.news import news_bp
app.register_blueprint(news_bp)
app.run(debug=True)