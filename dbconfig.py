class Config:

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True
    TESTNG = True
    DATABASE_URL = 'postgresql://postgres:root@localhost/StackOverflow'

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = 'postgresql://postgres:root@localhost/StackOverflow_test'