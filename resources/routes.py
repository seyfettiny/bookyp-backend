from .book import BooksApi, BookApi, BookDownloadApi
from .auth import SignupApi, LoginApi
from .review import BookReviews, BookReview
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
    # /api/book/<id>/reviews/
    api.add_resource(BookReviews, '/api/reviews')
    api.add_resource(BookReview, '/api/review/<id>')
    
    api.add_resource(BooksApi, '/api/books')
    api.add_resource(BookApi, '/api/book/')
    api.add_resource(BookDownloadApi,'/api/files/<file>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
    
