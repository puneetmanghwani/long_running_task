from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# endpoint to upload the file then extract the data and save it to database.
class uploadFileView(APIView):
    def post(self, request, format=None):
        try:
            print(request.FILES['file'])
        except KeyError:
            return Response(data='No File',status=status.HTTP_400_BAD_REQUEST)        
        return Response(data='d')

# endpoint to export the data saved in a file.
class dataExportView(APIView):
    def get(self, request, format=None):
        pass

# endpoint to upload the file of teams and then extract and save data in database.
class uploadTeamsView(APIView):
    def post(self, request, format=None):
        pass

# endpoint to terminate the ongoing task.
class terminateView(APIView):
    def post(self, request, format=None):
        pass