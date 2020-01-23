from flask_restplus import Namespace, Resource, fields
from app.main.models.tweet import Tweet
from config import Config
from flask_sqlalchemy import SQLAlchemy
from app import db

api = Namespace('tweets')
tweet = api.model('Tweet', {
    'text': fields.String,
    'id': fields.Integer,
    'created_at': fields.DateTime
    })

tweet_list = api.model('TweetList', {
    'tweets': fields.List(fields.Nested(tweet))
    })

new_tweet = api.model('Tweet', {
    'text': fields.String(required=True)
    })

@api.route('/<int:tweet_id>')
@api.response(404, 'Tweet not found')
@api.param('tweet_id', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.marshal_with(tweet, 200)
    def get(self, tweet_id):
        tweet = db.session.query(Tweet).get(tweet_id)
        return tweet

    @api.marshal_with(tweet,200)
    def delete(self, tweet_id):
        tweet_to_delete = Tweet.query.filter_by(id=tweet_id).first()
        db.session.delete(tweet_to_delete)
        db.session.commit()

    @api.marshal_with(tweet, 200)
    @api.expect(new_tweet, validate=True)
    def patch(self, tweet_id):
        tweet_received = api.payload()
        tweet = Tweet.query.filter_by(id=tweet_id).first()
        tweet.name = tweet_received['name']


@api.route('')
@api.response(201, 'Tweet added successfuly')
@api.response(422, 'Invalid tweet')
class TweetResource(Resource):
    @api.marshal_with(tweet, code=201)
    @api.expect(tweet, validate=True)
    def post(self):
        text = api.payload["text"]
        if len(text) > 0:
            tweet = Tweet()
            tweet.text = text
            db.session.add(tweet)
            db.session.commit()
            return tweet, 201
        else:
            return abort(422, "Tweet text can't be empty")

    @api.marshal_with(tweet_list, code=201)
    def get(self):
        tweets = db.session.query(Tweet).all()
        if tweets is not None:
            return tweets, 201
        return abort(422, "No tweets to return")

