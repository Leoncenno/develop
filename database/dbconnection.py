from enum import unique
import psycopg2.extras
import psycopg2
import config
from decouple import config


dbhost = config('HOST')
dbdatabase = config('DATABASE')
dbuser = config('USER')
dbpassword = config('PASSWORD')


class DbConnect():  # connect to the StackOverflow database
    def __init__(self):
        """Connect to the StackOverflow Database Server"""

        try:
            self.conn = None
            params = config  # read connection parameters

            # connect to StackOverflow server
            print('connecting to StackOverflow Database...')
            self.conn = psycopg2.connect(
                host=dbhost,
                database=dbdatabase,
                user=dbuser,
                password=dbpassword)

            self.cur = self.conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)  # create a cursor
            self.conn.autocommit = True

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)