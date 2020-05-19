# Post

from google.appengine.ext import ndb


class Post(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    subject = ndb.StringProperty(required=True)
    comment = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)

    replies = []
    numOfReplies = 0

    @staticmethod
    def get(id):
        return ndb.Key(urlsafe=id).get()

    @staticmethod
    def get_user_posts(user):
        return Post.query(Post.user == user).order(-Post.hora)
