import os
class config(object):
    """config file lol did u expect anything else?"""
    SECRET_KEY = os.environ.get('SECRET_KEY')or 'u_know_my_name_and_it_is_the_key'


