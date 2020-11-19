from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from transfer.views import uploadFileView,dataExportView,uploadTeamsView,terminateView


urlpatterns = [
    path('uploadfile/', uploadFileView.as_view(),name="uploadFile"),
    path('dataexport/', dataExportView.as_view(),name="dataExport"),
    path('uploadteams/', uploadTeamsView.as_view(),name="uploadTeams"),
    path('terminate/', terminateView.as_view(),name="terminate"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)