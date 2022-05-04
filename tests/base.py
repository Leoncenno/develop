import unittest
from app.app import app
from app.models import Models
from database.dboperations import DbOperations
from flask import json
from database.dbconnection import DbConnection
from decouple import config, Config
from tests.__init__ import (questions, get_all_questions, get_answers_for_one_question, get_one_question, post_answer, post_question,\
                empty_string_answer_post, empty_string_description_post, empty_string_question_post, empty_string_update_question,\
                wrong_input_answer, wrong_input_description, wrong_input_login, wrong_input_question, wrong_input_sign_up,\
                wrong_input_update_question, sign_up, missing_data_login, missing_data_sign_up, user_data)
from dbconfig import TestConfig


app.config.from_object('dbconfig.TestConfig')

db = DbConnection()
cur = db.cur


class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def signup_user(self, sign_up):
        response = self.client.post('/register', data = json.dumps(sign_up), content_type = 'application/json')
        return response

    def wrong_user_signup(self, wrong_input_sign_up):
        response = self.client.post('/register', data = json.dumps(wrong_input_sign_up), content_type = 'application/json')
        return response

    def missing_field_signup(self, missing_data_sign_up):
        response = self.client.post('/register', data = json.dumps(missing_data_sign_up), content_type = 'application/json')
        return response

    def signin_user(self, user_data):
        response = self.client.post('/login', data = json.dumps(user_data), content_type = 'application/json')
        return response

    def user_token(self, user_data):
        response = self.client.post('/login', data = json.dumps(user_data), content_type = 'application/json')
        response_data = json.loads(response.data.decode())
        return response_data["Token"]

    def wrong_login_input(self, wrong_input_login):
        response = self.client.post('/login', data = json.dumps(wrong_input_login), content_type = 'application/json')
        return response

    def missing_field_login(self, missing_data_login):
        response = self.client.post('/login', data = json.dumps(missing_data_login), content_type = 'application/json')
        return response

    def post_a_question(self, post_question):
        response = self.client.post('/api/v1/questions', headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(post_question), content_type = 'application/json')
        return response

    def empty_string_question(self, empty_string_question_post):
        response = self.client.post('/api/v1/questions',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(empty_string_question_post), content_type = 'application/json')
        return response

    def wrong_question_input(self, wrong_input_question):
        response = self.client.post('/api/v1/questions',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(wrong_input_question), content_type = 'application/json')
        return response

    def empty_string_description(self, empty_string_description_post):
        response = self.client.post('/api/v1/questions',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(empty_string_description_post), content_type = 'application/json')
        return response

    def wrong_description_input(self, wrong_input_description):
        response = self.client.post('/api/v1/questions',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(wrong_input_description), content_type = 'application/json')
        return response

    def empty_string_update_question(self, empty_string_update_question):
        response = self.client.post('/api/v1/questions/1',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(empty_string_update_question), content_type = 'application/json')
        return response

    def wrong_question_update_input(self, wrong_input_update_question):
        response = self.client.post('/api/v1/questions/1',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(wrong_input_update_question), content_type = 'application/json')
        return response
    
    def get_all_questions(self):
        response = self.client.get('/api/v1/questions',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,content_type = 'application/json')
        return response

    def get_all_questions_no_authorization(self):
        response = self.client.get('/api/v1/questions',content_type = 'application/json')
        return response

    def get_one_question(self):
        response = self.client.get('/api/v1/questions/1',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,content_type = 'application/json')
        return response

    def post_an_answer(self, post_answer):
        response = self.client.post('/api/v1/questions/1/answers', headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(post_answer), content_type = 'application/json')
        return response

    def empty_string_answer(self, empty_string_answer_post):
        response = self.client.post('/api/v1/questions/1/answers',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(empty_string_answer_post), content_type = 'application/json')
        return response

    def wrong_answer_input(self, wrong_input_answer):
        response = self.client.post('/api/v1/questions/1/answers',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,data = json.dumps(wrong_input_answer), content_type = 'application/json')
        return response

    def get_answers_for_a_question(self):
        response = self.client.get('/api/v1/questions/<id>/answers',headers={'Authorization': 'Bearer '+ self.user_token(user_data)}\
        ,content_type = 'application/json')
        return response
