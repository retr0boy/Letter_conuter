import os
basedir = os.path.abspath(os.path.dirname(__file__))
class config(object):
    """config file lol did u expect anything else?"""
    SECRET_KEY = os.environ.get('SECRET_KEY')or 'u_know_my_name_and_it_is_the_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

