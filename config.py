import os

class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = 'replace-this-with-a-secure-random-value'
    # Put any configurations here that are common across all environments

    # Testint database - do not use in production
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqldb://{os.getenv('MYSQL_USER', 'pt_admin')}:"
        f"{os.getenv('MYSQL_PASSWORD', 'pt2017')}@"
        f"{os.getenv('MYSQL_HOST', 'localhost')}/"
        f"{os.getenv('MYSQL_DATABASE', 'proptrunk_db')}"
    )


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test_secret'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
