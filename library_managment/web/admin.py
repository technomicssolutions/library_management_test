from django.contrib import admin
from web.models import Student,Book,BookCategory

admin.site.register(Student)
admin.site.register(BookCategory)
admin.site.register(Book)