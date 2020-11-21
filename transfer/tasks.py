from __future__ import absolute_import, unicode_literals
from celery import shared_task,task
import csv
from transfer.models import taskData,uploadData,teamData,exportData
from django.db import transaction
import time
from celery.app.task import Task
import celery
import datetime
from celery.task.control import revoke


# shared task to get data from uploaded file
@shared_task(bind=True)
def extractDataFromFile(self,file):
	# atomic transaction so that if task not fullfilled it will be rolled back
	with transaction.atomic():
		file = open(file)
		read = csv.reader(file)
		for row in read:
			'''
			check status of current task if it is pausing than make the task an infinted loop
			till the status goes in proccessing or time runs out then it is revoked
			'''
			if celery.result.AsyncResult(self.request.id).state == 'PAUSING':
				pause_start_time = datetime.datetime.now()
				while(1):
					curr_time = datetime.datetime.now()

					# if time difference is greater than 15 minutes then task will be revoked
					if ( ( curr_time - pause_start_time ).seconds )/60 > 15 :
						revoke(self.request.id, terminate=True)
						break
					# if it is resumed then break the infinite loop
					if(celery.result.AsyncResult(self.request.id).state == 'PROCESSING'):
						break
			upload= uploadData(name=row[1],label=row[2],type=row[3])
			upload.save()
			
			
# shared task to get data from teams file
@shared_task(bind=True)
def makeTeamsFromFile(self,file):
	# atomic transaction so that if task not fullfilled it will be rolled back
	with transaction.atomic():
		file = open(file)
		read = csv.reader(file)
		for row in read:
			'''
			check status of current task if it is pausing than make the task an infinted loop
			till the status goes in proccessing or time runs out then it is revoked
			'''
			if celery.result.AsyncResult(self.request.id).state == 'PAUSING':
				pause_start_time = datetime.datetime.now()
				while(1):
					curr_time = datetime.datetime.now()
					# if time difference is greater than 15 minutes then task will be revoked
					if ( ( curr_time - pause_start_time ).seconds )/60 > 15 :
						revoke(self.request.id, terminate=True)
						break
					# if it is resumed then break the infinite loop
					if(celery.result.AsyncResult(self.request.id).state == 'PROCESSING'):
						break
			team= teamData(name=row[1],description=row[2],managers=row[3],members=row[4])
			team.save()
			

# shared task to make a csv file in storage 
@shared_task(bind=True)
def exportDataFromFile(self):
	# atomic transaction so that if task not fullfilled it will be rolled back
	with transaction.atomic():
		data = exportData.objects.all().values_list()
		file_writer = csv.writer(open(f"./Exports/{self.request.id}.csv","w"))
		for row in data:
			'''
			check status of current task if it is pausing than make the task an infinted loop
			till the status goes in proccessing or time runs out then it is revoked
			'''
			if celery.result.AsyncResult(self.request.id).state == 'PAUSING':
				pause_start_time = datetime.datetime.now()
				while(1):
					curr_time = datetime.datetime.now()
					# if time difference is greater than 15 minutes then task will be revoked
					if ( ( curr_time - pause_start_time ).seconds )/60 > 15 :
						revoke(self.request.id, terminate=True)
						break
					# if it is resumed then break the infinite loop
					if(celery.result.AsyncResult(self.request.id).state == 'PROCESSING'):
						break
			file_writer.writerow(row)
			


	