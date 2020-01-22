from flask_restplus import Namespace, Resource, fields
from app.db import tweet_repository


api = Namespace('tweets')
tweet = api.model('Tweet', {
    'text': fields.String,
    'id': fields.Integer,
    'created_at': fields.DateTime
    })

@api.route('/<int:identifiant>/<tweet_text>')
@api.response(404, 'Tweet not found')
@api.param('identifiant', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.marshal_with(tweet)
    def get(self, identifiant):
        tweet = tweet_repository.get(identifiant)
        if tweet is None:
            api.abort(404)
        else:
            return tweet

    def post(self, tweet_text):
        tweet = Tweet(tweet_text)
        tweet_repository.add(tweet)
        return 200



