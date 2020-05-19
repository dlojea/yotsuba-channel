# Like

from google.appengine.ext import ndb

from post import Post

class Like(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    post_id = ndb.KeyProperty(kind=Post)
    user = ndb.StringProperty(required=True)

    @staticmethod
    def get(post_id, user):
        return Like.query(Like.post_id == post_id, Like.user == user).get()
    @staticmethod
    def get_all(post_id):
        return Like.query(Like.post_id == post_id)

