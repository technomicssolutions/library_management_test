from django.conf.urls import patterns,url
from web import views
urlpatterns = patterns('',
	url(r'login/$', views.Login.as_view(), name='login'),
    url(r'logout/$',views.Logout.as_view(), name='logout'),
	url(r'^$', 'web.views.home', name='home'),
	url(r'^deletestudent/(?P<student_id>\d+)/$', views.DeleteStudent.as_view(), name='deletestudent'),
	url(r'^deletebook/(?P<book_id>\d+)/$', views.DeleteBook.as_view(), name='deletebook'),
	url(r'^deletebookcategory/(?P<book_category>\d+)/$', views.DeleteBookCategory.as_view(), name='deletebookcategory'),
	url(r'^edit_student/(?P<student_id>\d+)/$', views.EditStudent.as_view(), name='edit_student'),
	url(r'^edit_book/(?P<book_id>\d+)/$', views.EditBook.as_view(), name='edit_book'),
	url(r'^edit_bookcategory/(?P<book_category>\d+)/$', views.EditBookCategory.as_view(), name='edit_bookcategory'),
	url(r'^students/$', views.StudentView.as_view(), name='students'),
	url(r'^books/$', views.BookView.as_view(), name='books'),
	url(r'^bookcategories/$', views.BookCategoryView.as_view(), name='bookcategories'),
	url(r'^show_issue/$', views.IssueView.as_view(), name='show_issue'),
	url(r'^add_students/$','web.views.add_students',name='add_students'),
	url(r'^add_book/$','web.views.add_books',name='add_book'),
	url(r'^add_bookcategory/$','web.views.add_bookcategory',name='add_bookcategory'),
	url(r'^issuebook/$', views.IssueBook.as_view(), name='issuebook'),
	url(r'^show_book_category/(?P<bookcategory_id>\d+)/$', views.ShowBookCategoryView.as_view() ,name='show_book_category'),
	url(r'^return/(?P<issue_id>\d+)/(?P<student_id>\d+)/(?P<book_id>\d+)/$', views.ReturnView.as_view(), name='return'),

	)