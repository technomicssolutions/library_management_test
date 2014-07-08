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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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

class IssueView(generic.ListView):
	template_name = 'web/show_issue.html'
	context_object_name = 'latest_issue_list'
	
	def get_queryset(self):
		issue = Issue.objects.order_by('date_of_issue')
		return issue

class ShowBookCategoryView(View):
	
	def get(self,request,*args,**kwargs):
		bookcategory_id = kwargs['bookcategory_id']
		bookcategory = BookCategory.objects.get(id=bookcategory_id)
		return render(request, 'web/show_book_category.html', {'bookcategory':bookcategory, })

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
		try:
			if request.method == "POST" :
				form = StudentForm(request.POST,instance=student)
				#print "form ==", form
				form.save()
				# return render(request, 'web/students.html',{'form':form,'student_id':student_id })
				return HttpResponseRedirect(reverse('students'))
		except (KeyError, TypeError) as e:
			print e

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
		try:
			if request.method == "POST" :
				form = BookForm(request.POST,instance=book)
				#print "form ==", form
				form.save()
				# return render(request, 'web/books.html',{'form':form,'book_id':book_id })
				return HttpResponseRedirect(reverse('books'))
		except (KeyError, TypeError) as e:
			print e

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
		try:
			if request.method == "POST" :
				form = BookCategoryForm(request.POST,instance=bookcategory)
				#print "form ==", form
				form.save()
				# return render(request, 'web/bookcategory.html',{'form':form,'book_category':book_category })
				return HttpResponseRedirect(reverse('bookcategory'))
		except (KeyError, TypeError) as e:
			print e

class IssueBook(View):
	
	def get(self,request,*args,**kwargs):
		students = Student.objects.all()
		books = Book.objects.filter(is_available=True)
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
		#print request.POST, 'hiiiii'
		if request.method == "POST":
			student_id  =  request.POST['student_id']
			student = Student.objects.get(id=student_id)
			if student.books_student_has <3:
				book_id = request.POST['book_id']	
				book = Book.objects.get(id=book_id)
				if book.is_available == True:
					book.is_available = False
					date_of_issue = datetime.now()
					date_of_return = datetime.now() + dt.timedelta(days=7)
					return_flag = False
					issue = Issue.objects.create(date_of_issue=date_of_issue, date_of_return=date_of_return, book=book, student=student, return_flag=return_flag)
					student.books_student_has = student.books_student_has + 1
					student.save()
					book.save()
					return HttpResponseRedirect(reverse('show_issue'))
			else :
				return render(request,'web/error.html',{})

class ReturnView(View):
	
	def get(self,request,*args,**kwargs):
		issue_id = kwargs['issue_id']
		issue = Issue.objects.get(id=issue_id)
		student_id = kwargs['student_id']
		student = Student.objects.get(id=student_id)
		book_id = kwargs['book_id']
		book = Book.objects.get(id=book_id)
		now = timezone.now()
		if now > issue.date_of_return:
			student.fine = student.fine + 5
		if student.books_student_has >0:
			book.is_available = True
			student.books_student_has = student.books_student_has - 1
			issue.return_flag = True
			issue.save()
			student.save()
			book.save()
			return HttpResponseRedirect(reverse('show_issue'))

class Login(View):

    def get(self, request, *args, **kwargs):
    	if request.user.is_authenticated():
    		return HttpResponseRedirect(reverse('home'))
        
        return render(request, 'web/login.html',{})

    def post(self, request, *args, **kwargs):

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print user
        if user and user.is_active:

            login(request, user)
        else:
            context = {
                'message' : 'Username or password is incorrect'
            }
            return render(request, 'web/login.html',context)
        context = {
            'Success_message': 'Welcome '+request.POST['username']
        }

        return render(request, 'web/home.html',context)

class Logout(View):

    def get(self, request, *args, **kwargs):

        logout(request)
        return HttpResponseRedirect(reverse('login'))
