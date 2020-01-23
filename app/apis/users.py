from flask_restplus import Namespace, Resource, fields
from app.main.models.user import User

api = Namespace('users')
user = api.model('User', {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'pseudo': fields.String
    })

@api.route('/<int:identifiant>')
@api.response(404, 'Tweet not found')
@api.param('identifiant', 'The user unique identifier')

class UserResource(Resource):
    @api.marshal_with(user)
    def get(self, identifiant):
        return 'user'
