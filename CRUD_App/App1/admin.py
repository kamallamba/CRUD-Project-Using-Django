from django.contrib import admin
from.models import StudentsInfo

# Register your models here.
@admin.register(StudentsInfo)
class StudentAdmin(admin.ModelAdmin):
    list_display=['Name','Roll_NO','Email']
