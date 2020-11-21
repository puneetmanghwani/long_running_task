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

@shared_task(bind=True)
def extractDataFromFile(self,file):
	with transaction.atomic():
		file = open(file)
		read = csv.reader(file)
		for row in read:
			if celery.result.AsyncResult(self.request.id).state == 'PAUSING':
				pause_start_time = datetime.datetime.now()
				while(1):
					curr_time = datetime.datetime.now()
					if ( ( curr_time - pause_start_time ).seconds )/60 > 15 :
						revoke(self.request.id, terminate=True)
						break
					if(celery.result.AsyncResult(self.request.id).state == 'PROCESSING'):
						break

			upload= uploadData(name=row[1],label=row[2],type=row[3])
			upload.save()
			time.sleep(0.1)
		
@shared_task(bind=True)
def makeTeamsFromFile(self,file):
	with transaction.atomic():
		file = open(file)
		read = csv.reader(file)
		for row in read:
			if celery.result.AsyncResult(self.request.id).state == 'PAUSING':
				pause_start_time = datetime.datetime.now()
				while(1):
					curr_time = datetime.datetime.now()
					if ( ( curr_time - pause_start_time ).seconds )/60 > 15 :
						revoke(self.request.id, terminate=True)
						break
					if(celery.result.AsyncResult(self.request.id).state == 'PROCESSING'):
						break
			team= teamData(name=row[1],description=row[2],managers=row[3],members=row[4])
			team.save()

@shared_task(bind=True)
def exportDataFromFile(self):
	with transaction.atomic():
		data = exportData.objects.all().values_list()
		with open('./csvfile.csv','w+') as file:
			file_writer=csv.writer(file)
			for row in data:
				if celery.result.AsyncResult(self.request.id).state == 'PAUSING':
					pause_start_time = datetime.datetime.now()
					while(1):
						curr_time = datetime.datetime.now()
						if ( ( curr_time - pause_start_time ).seconds )/60 > 15 :
							revoke(self.request.id, terminate=True)
							break
						if(celery.result.AsyncResult(self.request.id).state == 'PROCESSING'):
							break
				file_writer.writerow(row)

# @task(name="transfer.change_status",bind=True)
# def updateTaskStatus(self,task_id,finalStatus):
# 	with transaction.atomic():
# 		print('reached')
# 		self.update_state(task_id=task_id,status=finalStatus)

	