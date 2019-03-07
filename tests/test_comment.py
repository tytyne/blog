from app.models import Comment,User,Post
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_post = post(id=1,post_title='Test',post_content='This is a test post',category="success",user = self.user_James)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_James,post=self.new_post)

    def tearDown(self):
        post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_James)
        self.assertEquals(self.new_comment.post,self.new_post)