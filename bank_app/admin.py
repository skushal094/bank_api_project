from django.contrib import admin
from . import models

admin.site.register(models.Bank)
admin.site.register(models.State)
admin.site.register(models.Location)
admin.site.register(models.Branch)