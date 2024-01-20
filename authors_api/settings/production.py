from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")
