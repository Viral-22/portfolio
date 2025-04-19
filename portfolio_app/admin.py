# Register your models here.
from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models


class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()}  # Enables CKEditor in Admin
    }

admin.site.register(Resume)
admin.site.register(Certificate)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Contact)


