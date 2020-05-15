from django.contrib import admin

# Register your models here.

from account import models
admin.site.register(models.Account)
admin.site.register(models.Classes)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Admin)
admin.site.register(models.Course)
