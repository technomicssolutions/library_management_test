from django.db import models
import datetime
from django.utils import timezone

from django import forms
GENDER_CHOICES = (
    	('M', 'Male'),
    	('F', 'Female'),
    	)

class Student(models.Model):
	student_id = models.CharField(max_length=200, null=True, blank=True)
	name = models.CharField('Student Name', max_length=200)
	age = models.IntegerField('Age')
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
	address = models.CharField('Address', max_length=200)
	books_student_has = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name



class BookCategory(models.Model):
	
	book_category = models.CharField('Categories', null=True, max_length=200)
	

	class Meta:
		verbose_name_plural = "Book Categories"

	def __unicode__(self):
		return self.book_category



class Book(models.Model):
	book_id = models.CharField('Book Id', max_length=100, null=True)
	book_name = models.CharField('Book Name', max_length=200, null=True)
	book_category = models.ForeignKey(BookCategory, null=True, blank=True)
	date_of_issue = models.DateTimeField('date issued', null=True, blank=True)
	date_of_return = models.DateTimeField('return date',null=True, blank=True)
	student = models.ForeignKey(Student, null=True, blank=True)

	def __unicode__(self):
		return self.book_name

class Issue(models.Model):
	book = models.ForeignKey(Book,null=True, blank=True)
	student = models.ForeignKey(Student,null=True, blank=True)
	date_of_issue = models.DateTimeField('date issued', null=True, blank=True)
	date_of_return = models.DateTimeField('return date',null=True, blank=True)
	