from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from transfer.views import uploadFileView,dataExportView,uploadTeamsView,terminateView,pauseUploadView,resumeUploadView,pauseExportView,resumeExportView,pauseTeamView,resumeTeamView


urlpatterns = [
    path('uploadfile/', uploadFileView.as_view(),name="uploadFile"),
    path('dataexport/', dataExportView.as_view(),name="dataExport"),
    path('uploadteams/', uploadTeamsView.as_view(),name="uploadTeams"),
    path('terminate/', terminateView.as_view(),name="terminate"),
    path('pauseupload/', pauseUploadView.as_view(),name="pauseupload"),
    path('resumeupload/', resumeUploadView.as_view(),name="resumeupload"),
    path('pauseexport/', pauseExportView.as_view(),name="pauseexport"),
    path('resumeexport/', resumeExportView.as_view(),name="resumeexport"),
    path('pauseuploadteam/', pauseTeamView.as_view(),name="pauseuploadteam"),
    path('resumeuploadteam/', resumeTeamView.as_view(),name="resumeuploadteam"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)