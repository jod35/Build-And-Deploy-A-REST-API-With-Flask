import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils.db import db
from werkzeug.security import generate_password_hash
from ..models.users import User


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app=create_app(config=config_dict['testing'])

        self.appctx=self.app.app_context()

        self.appctx.push()

        self.client=self.app.test_client()

        db.create_all()


    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app=None

        self.client =None


    def test_user_registration(self):

        data={
            "username":"testuser",
            "email":"testuser@company.com",
            "password":"password"
        }

        response=self.client.post('/auth/signup',json=data)

        user=User.query.filter_by(email="testuser@company.com").first()

        assert user.username == "testuser"


        assert response.status_code == 201


    def test_login(self):

        data={
            "email":"testuser@gmail.com",
            "password":"password"
        }
        response=self.client.post('/auth/login',json=data)


        assert response.status_code == 400