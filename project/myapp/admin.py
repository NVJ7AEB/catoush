from django.contrib import admin
from myapp.models import Users
from myapp.models import School
from myapp.models import Department
from myapp.models import Course
from myapp.models import Year
from myapp.models import QuestionPaper

# Register your models here.

admin.site.register(Users)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(QuestionPaper)
