"""
This file has the database definitions. 
Since we used MongoDB for database; there isn't any need to do migration or synch after the changes unlikely sqlite.

If you add a field in database, the only thing you have to do is adding it here with correct Field() object definition such as 'StringField()'.

If make you a field which is in another field, you have to make another class which inherits EmbeddedDocument Class::

	#In database;    
		"tweets": [
	        {
	            "user": "user_name",
	            "id": "tweet_id"
	        },...]
	
	#Add this to the relevant model;
	tweets = ListField(EmbeddedDocumentField(Tweets))

	#Then define that embedded document;
	class Tweets(EmbeddedDocument):
		user = StringField()
		id = StringField()

.. seealso:: http://mongoengine.org/


:Contents:
"""

from django.db import models

from datetime import datetime, timedelta

from mongoengine import * #Document and EmbeddedDocument classes come from here.

class Tweets(EmbeddedDocument):
	"""
	This model contains the details of tweets about relevant event. 
	It inherits the Document Class from MongoEngine.
	"""
	user = StringField()
	id = StringField()


class Events(Document):
	"""
	It represents MongoDB structure and inherits the Document Class from MongoEngine.
	"""
	meta = {'collection' : 'lecl'}
	tweets = ListField(EmbeddedDocumentField(Tweets))
	date = DateTimeField()
	score = FloatField()
	Estimation = DateTimeField()
	keylist = ListField(StringField())	

	def linkDate(self):
		"""
		The links to events in a date are working in case the url encoded in '%d-%m-%Y' format.
		This method converts each date of event to this string format.
		So you can go to template and just write following code to create a link for a date::

			<a href="{{ event.linkDate }}/events">

		This is especially used in presenting event details.
		"""
		ld = self.date.strftime("%d-%m-%Y") #dates which can be used in links
		return ld

	def datestr(self):
		"""
		Only defines a string format to show in templates.
		"""
		ds = self.date.strftime("%d %B %Y %A")#to string format
		return ds

	def Estimationstr(self):
		"""Only defines a string format to show in templates."""
		es = self.Estimation.strftime("%d %B %Y - %H:%M")#to string format
		return es

	def timeLeft(self):
		"""
		Calculates the time left to the events.
		
		"""
		if self.Estimation > datetime.now():
			hl =  self.Estimation - datetime.now()
			#!IDEA!: add 'time left' string to hl.
		else:
			hl = "Het event is al geweest."
		return hl








