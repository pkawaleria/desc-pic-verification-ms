from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ImageModel(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_hash = db.Column(db.String(64), unique=True, nullable=False)
    is_ok = db.Column(db.Boolean, default=False)

    def __init__(self, image_hash, is_ok=False):
        self.image_hash = image_hash
        self.is_ok = is_ok
