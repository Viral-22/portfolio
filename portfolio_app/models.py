# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField# for using image in description
from ckeditor_uploader.fields import RichTextUploadingField



class Resume(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads_app/resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads_app/certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description =RichTextUploadingField() # Allows images & rich formatting i can use images in description
    image = models.ImageField(upload_to='uploads_app/blog_images/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    reason_to_contact = models.TextField()
    company_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name