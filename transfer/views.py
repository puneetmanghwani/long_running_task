from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transfer.models import taskData
from django.http import JsonResponse
from transfer import tasks

# endpoint to upload the file then extract the data and save it to database.
class uploadFileView(APIView):
    def post(self, request, format=None):
        try:
            onGoingtask = tasks.extractDataFromFile.delay(request.FILES['file'].temporary_file_path())
            task = taskData(task_id=onGoingtask.id)
            task.save()
            return Response(data={'task_id':task.task_id},status=status.HTTP_200_OK)   
        except KeyError:
            return Response(data='No File',status=status.HTTP_400_BAD_REQUEST)        

# endpoint to export the data saved in a file.
class dataExportView(APIView):
    def get(self, request, format=None):
        onGoingtask = tasks.exportDataFromFile.delay()
        task = taskData(task_id=onGoingtask.id)
        task.save()
        return Response(data={'task_id':task.task_id},status=status.HTTP_200_OK)
# endpoint to upload the file of teams and then extract and save data in database.
class uploadTeamsView(APIView):
    def post(self, request, format=None):
        try:
            onGoingtask = tasks.makeTeamsFromFile.delay(request.FILES['file'].temporary_file_path())
            task = taskData(task_id=onGoingtask.id)
            task.save()
            return Response(data={'task_id':task.task_id},status=status.HTTP_200_OK)   
        except KeyError:
            return Response(data='No File',status=status.HTTP_400_BAD_REQUEST)        
        return Response(data='Success')

# endpoint to terminate the ongoing task.
class terminateView(APIView):
    def post(self, request, format=None):
        pass