from django.conf.urls import patterns,url
from web import views
urlpatterns = patterns('',
	url(r'^manage_students/$','web.views.manage_students',name='manage_students'),
	url(r'^manage_book/$','web.views.manage_books',name='manage_book'),
	#(r'^/login/$', 'django.contrib.auth.views.login',
      #{'template_name': 'web/login.html', 'authentication_form': LoginForm}),
	)