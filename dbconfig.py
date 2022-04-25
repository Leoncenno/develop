class Config:

    DEBUG = False

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = 'postgresql://postgres:root@localhost/StackOverflow'