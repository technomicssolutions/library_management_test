from web.models import Student,Book#,BookCategory,Book
from django.forms import ModelForm
from django import forms
class StudentForm(ModelForm):	
	class Meta:
		model = Student
		fields = ['student_id','name','age','gender','address']
#class BookCategoryForm(ModelForm):
	#class Meta:
		#model = BookCategory
		#fields = ['student_id','category']
class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['book_id','book_name']
#class LoginForm(forms.Form):
	#username = forms.CharField(widget=forms.TextInput)
	#password = forms.CharField(widget=forms.PasswordInput)
	