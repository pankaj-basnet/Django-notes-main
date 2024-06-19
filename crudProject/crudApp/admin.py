from django.contrib import admin
from .models import Teacher, Student

# Register your models here.

admin.site.register(Student)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id', 'name','age','email','address']
    list_display_links = ['name']
    list_filter = ['name', 'age']
    # list_per_page = 2
    search_fields = ['name']
    ordering = ['id']
