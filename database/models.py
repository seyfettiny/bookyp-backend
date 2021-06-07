from .db import db
import mongoengine_goodjson as gj
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash


class Book(gj.Document):
    title = db.StringField(required=True)
    description = db.StringField()
    isbn = db.IntField(unique=True)
    pages = db.IntField()
    file = db.StringField()
    cover = db.StringField()
    aiFile = db.StringField()
    audioFile = db.StringField()
    publishDate = db.DateTimeField(
        default=datetime.now().replace(microsecond=0))
    authors = db.ListField(db.StringField())
    categories = db.ListField(db.StringField())
    added_by = db.ReferenceField('User')
    reviews = db.ListField(db.ReferenceField('Review'))


class User(gj.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    books = db.ListField(db.ReferenceField(
        'Book', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Book, 'added_by', db.CASCADE)


class Review(gj.Document):
    title = db.StringField()
    content = db.StringField()
    rating = db.IntField()
    added_by = db.ReferenceField('User')
    publishDate = db.DateTimeField(
        default=datetime.now().replace(microsecond=0))
    book = db.ReferenceField('Book')


User.register_delete_rule(Review, 'added_by', db.CASCADE)
Book.register_delete_rule(Review, 'reviews', db.PULL)
