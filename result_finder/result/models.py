from django.db import models

# Create your models here.

class State(models.Model):
    state = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.state 

class Board(models.Model):
    board_name= models.CharField(max_length=100)
    board_details = models.TextField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.board_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.course_name

class Student_detail(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photo/')
    roll_no = models.IntegerField()
    date_of_birth = models.DateField()
    fathers_name = models.CharField(max_length=40)
    mothers_name = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    hindi = models.IntegerField()
    sanskrit = models.IntegerField()
    math = models.IntegerField()
    scielce = models.IntegerField()
    social_scielce = models.IntegerField()
    english = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def total_mark(self):
        return self.hindi + self.sanskrit + self.math + self.scielce + self.social_scielce + self.english
