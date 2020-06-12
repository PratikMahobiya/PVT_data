from django.db import models

# Create your models here.
class emp_table(models.Model):
	empno = models.IntegerField()
	empname= models.CharField(max_length=25)
	salary= models.FloatField()
	designation= models.TextField()
	class Meta:
		db_table= "emp"
