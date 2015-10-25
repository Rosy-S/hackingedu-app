from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model): 
	__tablename__ = "users"
	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_name = db.Column(db.String(25), nullable=False)
	email = db.Column(db.String(25), nullable=False)
	password = db.Column(db.String(25), nullable=False)
	phone = db.Column(db.String(10), nullable=True)
	tutor_id = db.Column(db.Boolean, nullable=True)

	def __rep__(self): 
		return "<User = %s>" % (self.user_name)

class Class(db.Model): 
	__tablename__ = "classes"
	subject = db.Column(db.String(25), primary_key=True)

	def __rep__(self): 
		return "<Class subject %s" % (self.subject)

class Session(db.Model): 
	__tablename__ = "sessions"
	study_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	hours = db.Column(db.Integer)
	subject_class = db.Column(db.String, db.ForeignKey('classes.subject'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

	def __rep__(self): 
		return "<Session for Student ID %s" % (self.user_id)


def init_app():

    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)


def connect_to_db(app):
	# Configure to use our SQLite database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://admin:POQDIFCTPTAEKFFF@aws-us-east-1-portal.5.dblayer.com:10928/hackingedu'
	db.app = app
	db.init_app(app)


if __name__ == "__main__": 
	from server import app
	connect_to_db(app)
	print "Connected to DB."

# import pycps

# if __name__ == "__main__": 

# 	con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'hackingedu', 'sanchezrosy42@gmail.com', 'hackingedu123', '102214')