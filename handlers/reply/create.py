#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time

from webapp2_extras.users import users

from model.post import Post
from model.reply import Reply

class CreateReplyHandler(webapp2.RequestHandler):
    def post(self):
        post_id = self.request.get("id")
        comment = self.request.get("newReply")
        user = str(users.get_current_user().email())

        post_key = Post.get(post_id).key

        reply = Reply(post_id=post_key, comment=comment, user=user)
        reply.put()
        time.sleep(1)

        self.redirect("/post/show?id=" + post_id)

app = webapp2.WSGIApplication([
    ('/reply/create', CreateReplyHandler)
], debug=True)
