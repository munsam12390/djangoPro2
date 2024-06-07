from django.contrib import admin
from application1.models import employees

@admin.register(employees)
class employees(admin.ModelAdmin):
    list_display=['eid','ename','esal','design']

# Register your models here.
