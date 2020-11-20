from django.db import models


class taskData(models.Model):
	task_id = models.CharField(max_length=100)
	

class uploadData(models.Model):
	name = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	
class teamData(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    managers = models.IntegerField(default=0)
    members = models.IntegerField(default=0)

class exportData(models.Model):
	submitted_by= models.CharField(max_length=100)
	response_id= models.CharField(max_length=100)
	tag= models.CharField(max_length=100)