from django.contrib import admin
from transfer.models import uploadData,teamData,exportData,taskData

admin.site.register(taskData)
admin.site.register(uploadData)
admin.site.register(teamData)
admin.site.register(exportData)
