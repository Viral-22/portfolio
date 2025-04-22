from django.shortcuts import render, redirect ,HttpResponse,get_object_or_404
from .models import *
# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html',{'current_page': 'home'})

def resume(request):
        resume = Resume.objects.last()  # Get the latest resume
        certificates = Certificate.objects.all()
        return render(request, 'portfolio/resume.html', {'resume': resume, 'certificates': certificates,'current_page': 'resume'})

def project(request):
    return HttpResponse("project page")

def blog(request):
    blogs = BlogPost.objects.all()
    return render(request, 'portfolio/blog.html', {'blogs': blogs, 'current_page': 'project'})

def blog_detail(request, title):
    blog = get_object_or_404(BlogPost, title=title)
    return render(request, 'portfolio/blog_detail.html', {'blog': blog})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def social(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been successfully submitted.')
            return redirect('social_link')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = ContactForm()

    return render(request, 'portfolio/social.html', {
        'form': form,
        'current_page': 'social'
    })