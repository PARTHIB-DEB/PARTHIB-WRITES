import pytest
from conftest import ConfUserModel

new_data={
    "username": input("\nUsername : "),
    "email": input("\nEmail : "),
    "first_name": input("\nfirst-name : "),
    "last_name": input("\nlast-name : "),
    "password": input("\npassword : ")
}

upd_data={
    "username": "Pkxy123",
    "email": "pkd@gmail.com",
    "first_name": "parthib"
}

upd_pass={
    "password":"Xk1234!!"
}

log_data = {
    "username":upd_data.get("username"),
    "password":upd_pass.get("password")
}

@pytest.mark.django_db
class TestUserModel :
    
    def setup_method(self,method):
        self.user = ConfUserModel()
        
    def teardown_method(self,method):
        del self.user
        
    def test_create_a_user(self):
        self.user.create_a_user(**new_data)
    
    def test_update_a_user(self):
        self.user.update_a_user(data=upd_data,old_data=new_data)
    
    def test_update_a_user_password(self):
        self.user.update_a_user_password(data=upd_pass,old_data=new_data)
    
    def test_login_a_user(self):
        self.user.login_a_user(data=log_data,old_data=new_data)