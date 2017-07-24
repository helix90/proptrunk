class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

    # Testint database - do not use in production
    SQLALCHEMY_DATABASE_URI = 'sqlite://proptrunk.db'


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

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
