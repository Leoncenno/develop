from tests.base import TestUser
from tests.__init__ import (questions, wrong_input_login, wrong_input_sign_up, sign_up, user_data, missing_data_login, missing_data_sign_up)


class TestUser(TestUser):
    def test_signup_user(self):
        response = self.signup_user(sign_up)
        self.assertEqual(response.status_code, 201)

    def test_wrong_user_signup(self):
        response = self.wrong_user_signup(wrong_input_sign_up)
        self.assertEqual(response.status_code, 406)

    def test_missing_field_signup(self):
        response = self.missing_field_signup(missing_data_sign_up)
        self.assertEqual(response.status_code, 406)

    def test_signin_user(self):
        response = self.signin_user(user_data)
        self.assertEqual(response.status_code, 200)

    def test_wrong_login_input(self):
        response = self.wrong_login_input(wrong_input_login)
        self.assertEqual(response.status_code, 401)

    def test_missing_field_login(self):
        response = self.missing_field_login(missing_data_login)
        self.assertEqual(response.status_code, 406)