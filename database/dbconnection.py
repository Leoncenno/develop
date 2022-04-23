import psycopg2
import psycopg2.extras
from decouple import config


class DbConnection():  # connect to the StackOverflow database
    def __init__(self):
        """Connect to the StackOverflow Database Server"""

        try:
            self.conn = None
            params = config  # read connection parameters

            # connect to StackOverflow server
            print('connecting to StackOverflow Database...')
            self.conn = psycopg2.connect(
                host='localhost',
                database='StackOverflow',
                user='postgres',
                password='root')

            self.cur = self.conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)  # create a cursor
            self.conn.autocommit = True

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        create_table = (
            """CREATE TABLE IF NOT EXISTS user_details (user_id SERIAL PRIMARY KEY, first_name VARCHAR (50) NOT NULL, last_name VARCHAR (50) NOT NULL, email VARCHAR (150) NOT NULL, password VARCHAR (150) NOT NULL, date_of_birth VARCHAR NOT NULL, user_name VARCHAR (150) NOT NULL
            )
            """,
            """CREATE TABLE IF NOT EXISTS questions (question_id SERIAL PRIMARY KEY, question VARCHAR (1000) NOT NULL, description VARCHAR (1000) NOT NULL
            )
            """,
            """CREATE TABLE IF NOT EXISTS answers (answer_id SERIAL PRIMARY KEY, answer VARCHAR (1000) NOT NULL, question_id INTEGER
            )
            """)

        for table in create_table:
            self.cur.execute(table)
