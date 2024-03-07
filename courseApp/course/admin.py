from django.contrib import admin
from django.utils.html import mark_safe

from course.models import Category, Course
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    decription = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'





class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'update_date', 'active']
    search_fields = ['name', 'decription']
    list_display = ['id', 'name']
    readonly_fields = ['my_image']
    form =CourseForm

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img width='200' src='/static/{course.image.name}'/>")

    class Media:
        css = {
            'all': ['/static/css/style.css']
        }


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)

# Register your models here.
