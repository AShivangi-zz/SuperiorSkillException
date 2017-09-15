from django.db import models

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
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

#example of what will be created in Database
# CREATE TABLE website_question(
#     "id" serial NOT NULL PRIMARY KEY,
#     "question_text" varchar(200) Not NULL,
#     "pub_date" ddateTimeFiled('date published')
#
# );


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

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