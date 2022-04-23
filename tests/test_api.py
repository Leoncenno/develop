from tests.base import TestUser
from tests.base import (get_all_questions, get_answers_for_one_question, get_one_question, post_answer, post_question,\
                empty_string_answer_post, empty_string_description_post, empty_string_question_post, empty_string_update_question,\
                wrong_input_answer, wrong_input_description, wrong_input_question, wrong_input_update_question)

class TestApp(TestUser):
    def test_post_a_question(self):
        response = self.post_a_question(post_question)
        self.assertEqual(response.status_code, 201)

    def test_empty_string_question(self):
        response = self.empty_string_question(empty_string_question_post)
        self.assertEqual(response.status_code, 406)

    def test_wrong_question_input(self):
        response = self.wrong_question_input(wrong_input_question)
        self.assertEqual(response.status_code, 406)

    def test_empty_string_description(self):
        response = self.empty_string_description(empty_string_description_post)
        self.assertEqual(response.status_code, 406)

    def test_wrong_description_input(self):
        response = self.wrong_description_input(wrong_input_description)
        self.assertEqual(response.status_code, 406)

    def test_empty_string_update_question(self):
        response = self.empty_string_update_question(empty_string_update_question)
        self.assertEqual(response.status_code, 405)

    def test_wrong_question_update_input(self):
        response = self.wrong_question_update_input(wrong_input_update_question)
        self.assertEqual(response.status_code, 405)

    def test_post_an_answer(self):
        response = self.post_an_answer(post_answer)
        self.assertEqual(response.status_code, 201)

    def test_empty_string_answer(self):
        response = self.empty_string_answer(empty_string_answer_post)
        self.assertEqual(response.status_code, 406)

    def test_wrong_answer_input(self):
        response = self.wrong_answer_input(wrong_input_answer)
        self.assertEqual(response.status_code, 406)

    def test_get_all_questions(self):
        response = self.get_all_questions()
        self.assertEqual(response.status_code, 200)

    def test_get_all_questions_no_authorization(self):
        response = self.get_all_questions_no_authorization()
        self.assertEqual(response.status_code, 401)

    def test_get_answers_for_a_question(self):
        response = self.get_answers_for_a_question()
        self.assertEqual(response.status_code, 200)

    def test_get_one_question(self):
        response = self.get_one_question()
        self.assertEqual(response.status_code, 200)