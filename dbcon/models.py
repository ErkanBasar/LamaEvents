# """
# This file has the database definitions. 
# Since we used MongoDB for database; there isn't any need to do migration or synch after the changes unlikely sqlite.

# If you add a field in database, the only thing you have to do is adding it here with correct Field() object definition such as 'StringField()'.

# If make you a field which is in another field, you have to make another class which inherits EmbeddedDocument Class::

#         #In database;    
#                 "tweets": [
#                 {
#                     "user": "user_name",
#                     "id": "tweet_id"
#                 },...]

#         #Add this to the relevant model;
#         tweets = ListField(EmbeddedDocumentField(Tweets))

#         #Then define that embedded document;
#         class Tweets(EmbeddedDocument):
#                 user = StringField()
#                 id = StringField()

# .. see also:: http://mongoengine.org/


# :Contents:
# """

# from django.db import models

# from datetime import datetime, timedelta

# from mongoengine import * #Document and EmbeddedDocument classes come from here.
# """
# When I tried to remark the line before, the connection with the data disconnected, and i needed to rerun the server (localy) again. 6-7-2018
# """

# class Tweets(EmbeddedDocument):
#     """
#     This model contains the details of tweets about relevant event. 
#     It inherits the Document Class from MongoEngine.
#     """
#     user = StringField()
#     id = StringField()
# #       postags = StringField()
# #       date = DateTimeField()
# #       entities = StringField()
# #       text = StringField()
# #       date_references = StringField()


# class Events(DynamicDocument):
#     """
#     It represents MongoDB structure and inherits the Document Class from MongoEngine.
#     """
#     meta = {'collection' : 'lecl'}
#     tweets = ListField(EmbeddedDocumentField(Tweets))
#     #Date from DEvents
#     date = DateTimeField()
#     score = FloatField()
#     location = StringField()
#     #Estimation = DateTimeField()
#     entities = ListField(StringField())
#     cycle = StringField()
#     predicted = StringField()
#     eventtype = StringField()
#     periodicity = DictField()
#     #keyterms = ListField(ListField()) # In the second ListField, there is a string and an integer E.g. : [['string1', 1], ['string2', 2]]

#     def linkDate(self):
#         """
#         The links to events in a date are working in case the url encoded in '%d-%m-%Y' format.
#         This method converts each date of event to this string format.
#         So you can go to template and just write following code to create a link for a date::
#         <a href="{{ event.linkDate }}/events">
#         This is especially used in presenting event details.
#         """
#         ld = self.date.strftime("%d-%m-%Y") #dates which can be used in links
#         return ld

#     def datestr1(self):
#         """
#         Only defines a string format to show in templates.
#         (datestr split in three to show them seperately in the templates.)
#         """
#         ds1 = self.date.strftime("%A").title() 
#         return ds1

#     def datestr2(self):
#         ds2 = self.date.strftime("%d %B %Y") 
#         return ds2

#     def datestr3(self):
#         ds3 = self.date.strftime("%H.%M uur")
#         return ds3

#     def datestr4(self):
#         ds4 = self.date.strftime("%Y-%m-%d")
#         return ds4

#     def entities_str(self):
#         enti_str = ', '.join(self.entities) # --> gives l1, l2, l3
#         return enti_str

# #       def Estimationstr(self):
# #               """Only defines a string format to show in templates."""
# #               es = self.Estimation.strftime("%d %B %Y - %H:%M")#to string format
# #               return es

#     def timeLeft(self):
#         """
#         Calculates the time left to the events.
        
#         """
#         if self.date > datetime.now():
#                 hl =  self.date - datetime.now()
#                 #!IDEA!: add 'time left' string to hl.
#         else:
#                 hl = "Het event is al geweest."
#         return hl







