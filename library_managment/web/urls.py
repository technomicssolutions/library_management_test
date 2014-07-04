from django.conf.urls import patterns,url
from web import views
urlpatterns = patterns('',
	url(r'^home/$', 'web.views.home', name='home'),
	url(r'^deletestudent/(?P<student_id>\d+)/$', views.DeleteStudent.as_view(), name='deletestudent'),
	url(r'^deletebook/(?P<book_id>\d+)/$', views.DeleteBook.as_view(), name='deletebook'),
	url(r'^deletebookcategory/(?P<book_category>\d+)/$', views.DeleteBookCategory.as_view(), name='deletebookcategory'),
	url(r'^edit_student/(?P<student_id>\d+)/$', views.EditStudent.as_view(), name='edit_student'),
	url(r'^students/$', views.StudentView.as_view(), name='students'),
	url(r'^books/$', views.BookView.as_view(), name='books'),
	url(r'^bookcategories/$', views.BookCategoryView.as_view(), name='bookcategories'),
	url(r'^add_students/$','web.views.add_students',name='add_students'),
	url(r'^add_book/$','web.views.add_books',name='add_book'),
	url(r'^add_bookcategory/$','web.views.add_bookcategory',name='add_bookcategory'),
	#(r'^/login/$', 'django.contrib.auth.views.login',
      #{'template_name': 'web/login.html', 'authentication_form': LoginForm}),
	)