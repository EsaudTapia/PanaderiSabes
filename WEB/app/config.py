import os

class Config(object):
    SECRET_KEY='my_secret_key'
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #clave aleatoria de la aplicacion uwu
    SECRET_KEY = os.urandom(24)
    
    #definimos la ruta de laBD
    SQLALCHEMY_DATABASE_URI = 'mysql://SEGyDEV:shrek@localhost/panaderia'
    SECURITY_PASSWORD_SALT = 'passwordsaltsi'
    