# Post

from google.appengine.ext import ndb


class Post(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    subject = ndb.StringProperty()
    comment = ndb.StringProperty(required=True)

    replies = []
    numOfReplies = 0

    @staticmethod
    def get(request):
        try:
            id = request.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
