from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath('.'), '.env'))

class Config:
	SECRET_KEY = environ.get('SECRET_KEY')
	BABEL_DEFAULT_LOCALE = 'en'