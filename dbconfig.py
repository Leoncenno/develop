class Config:

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True
    TESTNG = False
    DATABASE_URL = 'postgresql://postgres:root@localhost/stackoverflow'

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = 'postgres://postgres:@localhost/stackoverflow'