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
from webapp2_extras.users import users
from model.post import Post
from model.reply import Reply


class UserPostsHandler(webapp2.RequestHandler):
    def get(self):
        user = str(users.get_current_user().email())
        url_user = users.create_logout_url("/")

        posts = Post.get_user_posts(user)

        for post in posts:
            replies = Reply.get_replies(post.key)
            post.replies = replies.fetch()[-5:]
            post.numOfReplies = replies.count()

        template_values = {
            "user": user,
            "url_user": url_user,
            "posts": posts
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/post/user', UserPostsHandler)
], debug=True)