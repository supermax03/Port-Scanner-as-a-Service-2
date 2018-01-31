class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin123@localhost:5433/spy'




class DevelopmentConfig(Config):
    DEBUG = True


app_config = {
    'development': DevelopmentConfig
}