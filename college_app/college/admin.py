from django.contrib import admin

from college.models import  *
# Register your models here.

admin.site.register(College)

admin.site.register(CollegeAdmin)

admin.site.register(Student)

admin.site.register(Teacher)