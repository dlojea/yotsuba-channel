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

from model.like import Like
from model.post import Post

class UnlikeHandler(webapp2.RequestHandler):
    def post(self):
        post_id = self.request.get("id")
        user = str(users.get_current_user().email())

        post_key = Post.get(post_id).key

        like = Like.get(post_key, user)
        like.key.delete()
        time.sleep(1)

        self.redirect("/post/show?id=" + post_id)

app = webapp2.WSGIApplication([
    ('/like/unlike', UnlikeHandler)
], debug=True)
