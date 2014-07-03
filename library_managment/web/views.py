# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from web.models import Student,Book#,BookCategory,Book
from django.shortcuts import get_object_or_404, render,render_to_response
from web.forms import StudentForm,BookForm#,HomeForm,LoginForm,BookCategoryForm,BookForm
from django.views.generic.base import View

#class Home(View):
	#def get(self,request):
		#if request.method == 'GET'
			#form = HomeForm()

#class login(View):
	#if request.method == 'POST':
		#formset = LoginForm()


def manage_students(request):
	if request.method == 'GET':
		form = StudentForm()
	else :
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Home Page coming soon :p")
	return render(request, 'web/manage_students.html', {"form":form, })

def manage_books(request):
	if request.method == 'GET':
		form = BookForm()
	else :
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Home Page coming soon :p")
	return render(request, 'web/manage_book.html', {"form":form, })