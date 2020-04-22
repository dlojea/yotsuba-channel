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
from webapp2_extras import jinja2
from model.post import Post
from model.reply import Reply


class MainHandler(webapp2.RequestHandler):
    def get(self):
        posts = Post.query().order(-Post.hora)
        jinja = jinja2.get_jinja2(app=self.app)

        for post in posts:
            replies = Reply.query(Reply.post_id == str(post.key.id()))
            post.replies = replies.order(Reply.hora).fetch()[-5:]
            post.numOfReplies = replies.count()

        template_values = {
            "posts": posts
        }

        self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)