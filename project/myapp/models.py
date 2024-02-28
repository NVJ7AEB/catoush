from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    # date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    # last_updated = models.DateTimeField(verbose_name='Last Updated', auto_now=True)

     # Add more fields as needed, such as first name, last name, etc.

    def __str__(self):
     return self.username
    
class School(models.Model):
  name = models.CharField(max_length=100)
  schoolid = models.IntegerField()

  def __str__(self):
     return self.name    


class Department(models.Model):
  name = models.CharField(max_length=100)
  departmentid = models.IntegerField()
  school = models.ForeignKey(School, on_delete=models.CASCADE)
    

  def __str__(self):
     return self.name
    
class Course(models.Model):
  name = models.CharField(max_length=100)
  coursecode = models.IntegerField()
  department = models.ForeignKey(Department, on_delete=models.CASCADE)    

  def __str__(self):
     return self.name

class Year(models.Model):
   yearid = models.DateField()

   def __str__(self):
     return self.yearid.strftime('%Y')


class QuestionPaper(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  year = models.ForeignKey(Year, on_delete=models.CASCADE)
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  pdf_file = models.FileField(upload_to='question_papers/')

  def __str__(self):
     return f"{self.course.name} - {self.course.coursecode}"
