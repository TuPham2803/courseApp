from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(max_length=255)
    decription = RichTextField(null=True)
    image = models.ImageField(upload_to='course/%Y/%m')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=255,unique=True)

class lesson(BaseModel):
    subject = models.CharField(max_length=255)
    decription = RichTextField(null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

# Create your models here.
