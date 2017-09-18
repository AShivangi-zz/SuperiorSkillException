import datetime

from django.db import models
from django.utils import timezone

# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
#
# The basics:
#
# Each model is a Python class that subclasses django.db.models.Model.
# Each attribute of the model represents a database field.
# With all of this, Django gives you an automatically-generated database-access API; see Making queries.


# The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).
# Each field takes a certain set of field-specific arguments (documented in the model field reference).
# For example, CharField (and its subclasses) require a max_length argument which specifies the size of the VARCHAR database field used to store the data.


# !!!! THREE STEP PROCESS TO MAKING CHANGES TO MODELS
# 1. Change your models (in models.py).
# 2. Run python manage.py makemigrations to create migrations for those changes
# 3. Run python manage.py migrate to apply those changes to the database.

"""The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. 
You’ll use this value in your Python code, and your database will use it as the column name."""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#example of what will be created in Database
# CREATE TABLE website_question(
#     "id" serial NOT NULL PRIMARY KEY,
#     "question_text" varchar(200) Not NULL,
#     "pub_date" ddateTimeFiled('date published')
#
# );

"""Each field is represented by an instance of a Field class – e.g.,
 CharField for character fields and DateTimeField for datetimes. 
 This tells Django what type of data each field holds."""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# example of what will be created in Database
# CREATE TABLE website_choice(
#     "id" serial NOT NULL PRIMARY KEY,
#     "question" varchar(200)
#     "votes" integer(0)
# );


# Model Example:
# from django.db import models
#
# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
#
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()