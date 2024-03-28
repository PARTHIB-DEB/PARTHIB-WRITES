import pytest
from conftest import ConfBlogModel

new_data={
    "title": input("\nBlog-Title : "),
    "catchline": input("\nBlog-Catchline : "),
    "thumbnail": input("\nBlog-Thumbnail : "),
    "script": input("\nBlog-Script : "),
}

upd_data={
    "title": "Updated Python Blog",
    "catchline": "Updated Catchline",
    "script": "Updated Script"
}



@pytest.mark.django_db
class TestUserModel :
    
    def setup_method(self,method):
        self.blog = ConfBlogModel()
        
    def teardown_method(self,method):
        del self.blog
        
    def test_create_a_user(self):
        self.blog.create_a_blog(**new_data)
    
    def test_update_a_user(self):
        self.blog.update_a_blog(data=upd_data,old_data=new_data)
        
    def test_retrieve_a_blog(self):
        self.blog.retrieve_a_blog(old_data=new_data)
    
    