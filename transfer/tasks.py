from __future__ import absolute_import, unicode_literals
from celery import shared_task
import csv
from transfer.models import taskData,uploadData,teamData,exportData
from django.db import transaction
import time

@shared_task(bind=True)
def extractDataFromFile(self,file):
	with transaction.atomic():
		file = open(file)
		read = csv.reader(file)
		for row in read:
			upload= uploadData(name=row[1],label=row[2],type=row[3])
			upload.save()
		
@shared_task(bind=True)
def makeTeamsFromFile(self,file):
	with transaction.atomic():
		file = open(file)
		read = csv.reader(file)
		for row in read:
			team= teamData(name=row[1],description=row[2],managers=row[3],members=row[4])
			team.save()

@shared_task(bind=True)
def exportDataFromFile(self):
	with transaction.atomic():
		data = exportData.objects.all().values_list()
		with open('./csvfile.csv','w+') as file:
			file_writer=csv.writer(file)
			for row in data:
				file_writer.writerow(row)

	