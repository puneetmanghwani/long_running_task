from django.db import models


class taskData(models.Model):
	task_id = models.CharField(max_length=100)
	status = models.CharField(max_length=50)

class uploadData(models.Model):
	task_id = models.ForeignKey(taskData,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	
class SampleModelForTeam(models.Model):
    task_id = models.ForeignKey(taskData,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    managers = models.IntegerField(default=0)
    members = models.IntegerField(default=0)
