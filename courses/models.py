from django.db import models
class Courses(models.Model):
    course_id =models.IntegerField()
    course_name =models.CharField(max_length = 20)
    student_id = models.ForeignKey()
    teacher_id= models.ForeignKey()
    topics = models.TextField()
    course_room= models.CharField(max_length=20)
    
    
    
    def __str__(self):
          return f"{self.course_name} {self.course_id}"

# Create your models here.
