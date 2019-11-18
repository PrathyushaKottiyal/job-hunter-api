from django.contrib import admin

from jobhunter_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Openings)

# Register your models here.
