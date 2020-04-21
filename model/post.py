# Comment

from google.appengine.ext import ndb

class Post(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    subject = ndb.StringProperty()
    comment = ndb.StringProperty(required=True)