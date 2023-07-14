import os


class Config(object):
    DEBUG = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_BACKEND_URL = os.environ.get('CELERY_BACKEND_URL', 'redis://localhost:6379/0')
    CELERY_ALWAYS_EAGER = False #Run celery tasks synchronously
    QUOTES_API_KEY = ''


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    QUOTES_API_KEY = 'E4e2-c8FjLdNmu-oD151'


class StageConfig(Config):
    DEBUG = False
    ENV = 'stage'
    QUOTES_API_KEY = 'E4e2-c8FjLdNmu-oD151'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    CELERY_ALWAYS_EAGER = True #Run celery tasks synchronously
    QUOTES_API_KEY = 'E4e2-c8FjLdNmu-oD151'


class TestingConfig(Config):
    DEBUG = True
    ENV = 'test'
    QUOTES_API_KEY = 'E4e2-c8FjLdNmu-oD151'
