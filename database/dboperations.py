from dbconnection import DbConnect


class DbOperations(DbConnect):
    def create_questions_table(self):
        """"Create table to store questions"""
        questions_table = (
                "CREATE TABLE IF NOT EXISTS quesstions (question_id SERIAL PRIMARY KEY, question VARCHAR (1000) NOT NULL, description VARCHAR (1000) NOT NULL)")
        self.cur.execute(questions_table)

    def create_answers_table(self):
        """"Create a table to store question answers"""
        answers_table = (
                "CREATE TABLE IF NOT EXISTS answers (answer_id SERIAL PRIMARY KEY, answer VARCHAR (1000) NOT NULL, question_id INTEGER)")
        self.cur.execute(answers_table)

    def create_user_details_table(self):
        """"Create table to store user details"""
        user_details_table = ("CREATE TABLE IF NOT EXISTS user_details (user_id SERIAL PRIMARY KEY, first_name VARCHAR (50) NOT NULL, last_name VARCHAR (50) NOT NULL, email VARCHAR (150) NOT NULL, password VARCHAR (150) NOT NULL, confirm_password VARCHAR (150)NOT NULL, date_of_birth VARCHAR NOT NULL, user_name VARCHAR (150) NOT NULL,)")
        self.cur.execute(user_details_table)

    def get_all_questions(self):
        self.cur.execute('SELECT * FROM questions')
        all_questions = self.cur.fetchall()
        return all_questions