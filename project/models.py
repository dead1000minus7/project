from project import db


class News(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=True)
    time = db.Column(db.String, nullable=True)
    seo_title = db.Column(db.String, nullable=True)
    seo_description = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    subtitle = db.Column(db.String, nullable=True)
    content_page = db.Column(db.String, nullable=True)
    short_link = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)