import random
import string

email = (''.join(random.sample(string.ascii_lowercase, k=5))) + "@gmail.com"
username = (''.join(random.sample(string.ascii_lowercase, k=5)))

questions = {"question": "What is a test?"}

get_all_questions = {}

get_one_question = {}

get_answers_for_one_question = {}

post_question = {"question": "What is your name?",
                 "description": "A new description name"}

empty_string_question_post = {"question": "", "description": "A new description name"}

empty_string_description_post = {"question": "What is your name?", "description": ""}

wrong_input_question = {"question": "12345", "description": "A new description name"}

wrong_input_description = {"question": "What is your name?", "description": "12345"}

post_answer = {"answer": "A new answer for the question."}

empty_string_answer_post = {"answer": ""}

wrong_input_answer = {"answer": "12345"}

update_question = {"question": "A new update for the question"}

empty_string_update_question = {"question": ""}

wrong_input_update_question = {"question": "123456"}

sign_up = {"firstname": "Smith", "lastname": "Okello", "email": 'smith@gmail.com',
                   "password": "okeli", "dateofbirth": "1994-04-20", "username": "smithokello"}

wrong_input_sign_up = {"firstname": "Smith", "lastname": "Okello", "email": "smith@gmail.com",
                   "password": "okeli", "dateofbirth": "1994-20-20", "username": "smith"}

missing_data_sign_up = {"firstname": "Smith", "lastname": "", "email": "smith@gmail.com",
                   "password": "okeli", "dateofbirth": "1994-04-20", "username": "smith"}

user_data = {"username": "smithokello", "password": "okeli"}

wrong_input_login = {"username": "smithokello", "password": "okelli"}

missing_data_login = {"username": "", "password": "okeli"}

