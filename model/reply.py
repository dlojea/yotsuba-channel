# Reply

from google.appengine.ext import ndb

from post import Post

class Reply(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    comment = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
    post_id = ndb.KeyProperty(kind=Post)

    @staticmethod
    def get_replies(post_id):
        return Reply.query(Reply.post_id == post_id).order(Reply.hora)

