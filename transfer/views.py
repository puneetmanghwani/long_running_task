from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transfer.models import taskData
from django.http import JsonResponse
from celery.task.control import revoke
from celery.app.task import Task
from transfer import tasks
from transfer.tasks import exportDataFromFile,extractDataFromFile,makeTeamsFromFile

# endpoint to upload the file then extract the data and save it to database.
class uploadFileView(APIView):
    def post(self, request, format=None):
        try:

            # adding the task to execute in background
            onGoingtask = tasks.extractDataFromFile.delay(request.FILES['file'].temporary_file_path())
            
            # saving task id in db
            task = taskData(task_id=onGoingtask.id)
            task.save()
            return Response(data={'task_id':task.task_id},status=status.HTTP_200_OK)   
        except KeyError:
            return Response(data='No File',status=status.HTTP_400_BAD_REQUEST)        

# endpoint to export the data saved in a file.
class dataExportView(APIView):
    def get(self, request, format=None):

        # adding the task to execute in background
        onGoingtask = tasks.exportDataFromFile.delay()

        # saving task id in db
        task = taskData(task_id=onGoingtask.id)
        task.save()
        return Response(data={'task_id':task.task_id},status=status.HTTP_200_OK)


# endpoint to upload the file of teams and then extract and save data in database.
class uploadTeamsView(APIView):
    def post(self, request, format=None):
        try:

            # adding task to execute in background
            onGoingtask = tasks.makeTeamsFromFile.delay(request.FILES['file'].temporary_file_path())
            
            # saving task id in db
            task = taskData(task_id=onGoingtask.id)
            task.save()
            return Response(data={'task_id':task.task_id},status=status.HTTP_200_OK)   
        except KeyError:
            return Response(data='No File',status=status.HTTP_400_BAD_REQUEST)        
        return Response(data='Success')

# endpoint to terminate the ongoing task.
class terminateView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:

                # stoping a particular task
                revoke(task_id, terminate=True)
                return Response(data={'status':'revoked'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)

# endpoint to pause the ongoing upload task
class pauseUploadView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:

                # updating the state of task by which we can pause the task by writing the custom logic in the extractDataFromFile by checking the status of this task
                Task.update_state(self=extractDataFromFile, task_id=task_id, state='PAUSING')
                return Response(data={'status':'paused'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)

# endpoint to resume the ongoing upload task
class resumeUploadView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:
                Task.update_state(self=extractDataFromFile, task_id=task_id, state='PROCESSING')
                return Response(data={'status':'resumed'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)

# endpoint to pause the ongoing export task
class pauseExportView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:
                # updating the state of task by which we can pause the task by writing the custom logic in the exportDataFromFile by checking the status of this task
                Task.update_state(self=exportDataFromFile, task_id=task_id, state='PAUSING')
                return Response(data={'status':'paused'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)

# endpoint to resume the ongoing export task
class resumeExportView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:
                Task.update_state(self=exportDataFromFile, task_id=task_id, state='PROCESSING')
                return Response(data={'status':'resumed'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)


# endpoint to pause the ongoing upload team task
class pauseTeamView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:
                # updating the state of task by which we can pause the task by writing the custom logic in the makeTeamsFromFile by checking the status of this id
                Task.update_state(self=makeTeamsFromFile, task_id=task_id, state='PAUSING')
                return Response(data={'status':'paused'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)

# endpoint to resume the ongoing upload team task
class resumeTeamView(APIView):
    def post(self, request, format=None):
        task_id=request.POST.get("task_id")
        if task_id:
            try:
                Task.update_state(self=makeTeamsFromFile, task_id=task_id, state='PROCESSING')
                return Response(data={'status':'resumed'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'status':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'error':'no task_id'},status=status.HTTP_400_BAD_REQUEST)


