from web.models import Student,Book,BookCategory,Issue
from django.forms import ModelForm
from django import forms
class StudentForm(ModelForm):	
	class Meta:
		model = Student
		fields = ['student_id','name','age','gender','address', 'id']
class BookCategoryForm(ModelForm):
	class Meta:
		model = BookCategory
		fields = ['book_category']
class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['book_id','book_name','book_category']
class IssueForm(ModelForm):
	class Meta:
		model = Issue
		fields = [ 'date_of_issue', 'date_of_return']

	