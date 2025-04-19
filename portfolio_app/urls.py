from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('project/', views.project, name='project'),
    path('blog/', views.blog, name='blog'),
    path('blog/<title>/', views.blog_detail, name='blog_detail'),
    path('social/', views.social, name='social_link'),

    ]