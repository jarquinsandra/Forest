"""

AUTOR: jarquinsandra


"""
# config/dev.py
from .default import *

APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:8889/Consensus'
SQLALCHEMY_ECHO = True