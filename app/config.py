class Config:
    POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'host': 'localhost',
        'port': '5432',
        'db': 'postgres'
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET = 'test'
