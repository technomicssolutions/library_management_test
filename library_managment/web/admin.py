from django.contrib import admin
from web.models import Student,Book,BookCategory,Issue

admin.site.register(Student)
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Issue)