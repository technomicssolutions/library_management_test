# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
import datetime as dt
from datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from web.models import Student,Book,BookCategory,Issue
from django.shortcuts import get_object_or_404, render,render_to_response
from web.forms import StudentForm,BookForm,BookCategoryForm,IssueForm
from django.views.generic.base import View
from django.views import generic


def home(request):
	return render(request, 'web/home.html', {})

def add_students(request):
	if request.method == 'GET':
		form = StudentForm()
	else :
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('students'))
	return render(request, 'web/add_students.html', {"form":form, })

def add_bookcategory(request):
	if request.method == 'GET':
		form = BookCategoryForm()
	else :
		form = BookCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('bookcategories'))
	return render(request, 'web/add_bookcategory.html', {"form":form, })

def add_books(request):
	if request.method == 'GET':
		form = BookForm()
	else :
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			# book_id = form.cleaned_data['book_id']
			# book_name = form.cleaned_data['book_name']
			# book_category = form.cleaned_data['book_category']
			# print timezone.now()
			# date_of_issue = datetime.now()
			# date_of_return = datetime.now() + dt.timedelta(days=7)
			# book = Book.objects.create(book_id=book_id, book_name=book_name, book_category=book_category ,date_of_issue=date_of_issue,date_of_return=date_of_return)
			return HttpResponseRedirect(reverse('books'))
	return render(request, 'web/add_book.html', {"form":form, })

class StudentView(generic.ListView):
	template_name = 'web/students.html'
	context_object_name = 'latest_student_list'
	
	def get_queryset(self):
		student = Student.objects.order_by('name')
		return student

class BookCategoryView(generic.ListView):
	template_name = 'web/bookcategory.html'
	context_object_name = 'latest_bookcategory_list'
	
	def get_queryset(self):
		bookcategory = BookCategory.objects.order_by('book_category')
		return bookcategory

class BookView(generic.ListView):
	template_name = 'web/books.html'
	context_object_name = 'latest_book_list'
	
	def get_queryset(self):
		book = Book.objects.order_by('book_name')
		return book



class DeleteStudent(View):
	
	def get(self,request,*args,**kwargs):
		student_id = kwargs['student_id']
		student = Student.objects.get(id=student_id)
		student.delete()
		return HttpResponseRedirect(reverse('students'))

class DeleteBook(View):
	
	def get(self,request,*args,**kwargs):
		book_id = kwargs['book_id']
		book = Book.objects.get(id=book_id)
		book.delete()
		return HttpResponseRedirect(reverse('books'))

class DeleteBookCategory(View):
	
	def get(self,request,*args,**kwargs):
		book_category = kwargs['book_category']
		bookcategory = BookCategory.objects.get(id=book_category)
		bookcategory.delete()
		return HttpResponseRedirect(reverse('bookcategory'))

class EditStudent(View):
	
	def get(self,request,*args,**kwargs):
		student_id = kwargs['student_id']
		student = Student.objects.get(id=student_id)
		if request.method == 'GET':
			form = StudentForm(instance=student)

		context = {
			"form":form,
			"student_id":student_id	
		}
		return render(request, 'web/edit_student.html', context)

	def post(self,request,*args,**kwargs):
		student_id = kwargs['student_id']
		student = Student.objects.get(id=student_id)
		if request.method == "POST" :
			form = StudentForm(request.POST,instance=student)
			#print "form ==", form
			form.save()
			return render(request, 'web/home.html',{'form':form,'student_id':student_id })

class EditBook(View):
	
	def get(self,request,*args,**kwargs):
		book_id = kwargs['book_id']
		book = Book.objects.get(id=book_id)
		if request.method == 'GET':
			form = BookForm(instance=book)

		context = {
			"form":form,
			"book_id":book_id	
		}
		return render(request, 'web/edit_book.html', context)

	def post(self,request,*args,**kwargs):
		book_id = kwargs['book_id']
		book = Book.objects.get(id=book_id)
		if request.method == "POST" :
			form = BookForm(request.POST,instance=book)
			#print "form ==", form
			form.save()
			return render(request, 'web/home.html',{'form':form,'book_id':book_id })

class EditBookCategory(View):
	
	def get(self,request,*args,**kwargs):
		book_category = kwargs['book_category']
		bookcategory = BookCategory.objects.get(id=book_category)
		if request.method == 'GET':
			form = BookCategoryForm(instance=bookcategory)

		context = {
			"form":form,
			"book_category":book_category	
		}
		return render(request, 'web/edit_bookcategory.html', context)

	def post(self,request,*args,**kwargs):
		book_category = kwargs['book_category']
		bookcategory = BookCategory.objects.get(id=book_category)
		if request.method == "POST" :
			form = BookCategoryForm(request.POST,instance=bookcategory)
			#print "form ==", form
			form.save()
			return render(request, 'web/home.html',{'form':form,'book_category':book_category })
class IssueBook(View):
	
	def get(self,request,*args,**kwargs):
		students = Student.objects.all()
		books = Book.objects.all()
		if request.method == "GET":
			formstudent = StudentForm()
			formbook = BookForm()
			context ={
			   "formstudent":formstudent,
			   "formbook":formbook,
		       "students":students,
		       "books":books,
			}
			return render(request,'web/issuebook.html',context)
	
	def post(self,request,*args,**kwargs):
		print request.POST, 'hiiiii'
		if request.method == "POST":
			name =  request.POST['student_id']
			#Student.objects.create(name=name)
			book = request.POST['book_id']	
			#Book.objects.create(book_name=book_name)
			form = IssueForm(request.POST)
			date_of_issue = datetime.now()
			date_of_return = datetime.now() + dt.timedelta(days=7)
			issue = Issue.objects.create(date_of_issue=date_of_issue, date_of_return=date_of_return)
			context ={
			   "form":form,
		       	
			}
			return render(request,'web/issuebook.html',context)