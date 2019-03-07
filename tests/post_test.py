from app.models import Comment, User,Post
from app import db
import unittest
class postTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'James', password = 'banana', email = 'james12@gmail.com')
        self.new_post = Post(id = 123, post_title = 'post', post_content = 'post content',category = 'general')

    def tearDown(self):
        User.query.delete()
        post.query.delete()
        Comment.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_post.id,123)
        self.assertEquals(self.new_post.title,'post')
        self.assertEquals(self.new_post.content,'post content')
        self.assertEquals(self.new_post.image,'post image')

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(post.query.all()) > 0)

    def test_get_posts(self):
        self.new_posts.save_post()
        post = post.get_post(123)
        self.assertTrue(post is not None)