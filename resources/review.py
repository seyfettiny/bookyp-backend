from flask import Response, request
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
from werkzeug.exceptions import InternalServerError
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import User, Review,Book
from flask_restful import Resource
from resources.errors import SchemaValidationError, ReviewNotExistsError

class BookReviews(Resource):
    def get(self):
        reviews = Review.objects().to_json()
        return Response(reviews, mimetype="application/json", status=200)
    
class BookReview(Resource):
    def get(self, id):
        try:
            review = Review.objects.get(id=id).to_json()
            return Response(review, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ReviewNotExistsError
        except Exception:
            raise InternalServerError
        
    @jwt_required()
    def post(self,id):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(id=id)
            body =request.get_json()
            user = User.objects.get(id=user_id)
            review = Review(**body,added_by=user,book=book)
            review.save()
            id = review.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError
        
    