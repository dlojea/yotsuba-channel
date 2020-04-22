# Reply

from google.appengine.ext import ndb

class Reply(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    post_id = ndb.StringProperty(required=True)
    comment = ndb.StringProperty(required=True)
