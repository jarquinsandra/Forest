"""

AUTOR: jarquinsandra


"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from app import db
import datetime

class TempSpectra(db.Model):
	__tablename__= 'temp_spectra'
	id = db.Column(db.Integer, primary_key = True)
	mz = db.Column(db.Float, unique=False, nullable=False)
	int_rel = db.Column(db.Float, unique=False, nullable=False)


class TempSpectra2(db.Model):
	__tablename__= 'temp_all_spectra'
	id = db.Column(db.Integer, primary_key = True)
	mz = db.Column(db.Float, unique=False, nullable=False)
	intensity = db.Column(db.Float, unique=False, nullable=False)
