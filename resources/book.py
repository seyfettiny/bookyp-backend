import os
from app import app
from flask import Response, request, send_from_directory
from database.models import Book, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, BookAlreadyExistsError, InternalServerError, \
    UpdatingBookError, DeletingBookError, BookNotExistsError


class BookDownloadApi(Resource):
    def get(self, file):
        return send_from_directory(app.config['BOOKS_FOLDER'],filename=file, as_attachment=True)

class BooksApi(Resource):
    def get(self):
        books = Book.objects().to_json()
        return Response(books, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            book = Book(**body, added_by=user)
            book.save()
            user.update(push__books=book)
            user.save()
            id = book.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise BookAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class BookApi(Resource):
    @jwt_required()
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Book.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingBookError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(id=id, added_by=user_id)
            book.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingBookError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            books = Book.objects.get(id=id).to_json()
            return Response(books, mimetype="application/json", status=200)
        except DoesNotExist:
            raise BookNotExistsError
        except Exception:
            raise InternalServerError
