import pytest
from conftest import ConfUserModel

data={
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
        self.user = ConfUserModel(data=data)
        
        
    def teardown_method(self,method):
        del self.user
    
    def test_create_a_user(self):
        return self.user.create_a_user()
    
    def test_update_a_user(self):
        self.user.update_a_user(data=upd_data,create_a_user=self.test_create_a_user())
    
    def test_update_a_user_passwprd(self):
        self.user.update_a_user_password(data=upd_pass,create_a_user=self.test_create_a_user())
    
    def test_login_a_user(self):
        self.user.login_a_user(data=log_data)