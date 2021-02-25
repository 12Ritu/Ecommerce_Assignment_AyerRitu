from django.db import models

# Create your models here.
class Properties(models.Model):
 id = models.IntegerField(primary_key=True)
 exam_date = models.DateField()
 exam_name = models. CharField(max_length=100)
 exam_description = models.TextField ()
 total_marks = models.FloatField ()
 pass_marks = models.FloatField()
 exam_status = models.BooleanField()