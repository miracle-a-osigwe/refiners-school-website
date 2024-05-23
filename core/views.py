from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Teacher, Student, Home, AboutUs
from . import forms
from post.models import Post, UpdateImage, get_post
from django.conf import settings

# Create your views here.

#set app name
app_name = 'core'

class IndexView(TemplateView):
    template_name = 'core/home.html'
    # model = Home

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        offer_tag = get_post('offer')
        event_tag = get_post('event')

        context = super().get_context_data(**kwargs)
        
        context['about_us'] = Post.objects.filter(published=True).filter(post_category=1).order_by('-date_published').first()
        context['offer'] = Post.objects.filter(published=True).filter(post_category=offer_tag) #.order_by('-date_published')
        context['events'] = Post.objects.filter(published=True).filter(post_category=event_tag).order_by('-date_published')


        
        images = UpdateImage.objects.filter(published=True).exclude(img_use=1)
        images = create_pairs(images)
        media_url = settings.MEDIA_URL
        # for image in images:
        #     if 'media' in image.img:
        #         image.img = str(image.img).replace('media/', '')
        if images:
            context['homepage_images'] = images
        context['media_url'] = media_url.replace('/', '')
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['about_us_data'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=5).first()) #.order_by('-data_published').first()
        context['mission'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=2).first()) #.order_by('-data_published')
        context['vision'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=3).first()) #.order_by('-date_published')
        context['core_values'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=8).first())
        context['school_anthem'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=9).first())
        context['school_creed'] = self.sort_data(Post.objects.filter(published=True).filter(post_category=7).first())

        return context
    
    def sort_data(self, text):
        if text is not None:
            text.content = text.content.replace('\r\n', ' <br> ')
            if 'refine' in str(text.content).lower():
                text.content = text.content.replace('REFINERS', '<strong>REFINERS</strong>') 
            return text
        return None

class AdmissionView(TemplateView):
    template_name = 'core/admission.html'

def admission(request):
    if request.method == 'POST':
        form1 = forms.CandidateInfo(request.POST)
        form2 = forms.CandidatePreviousSchool(request.POST)
        form3 = forms.ParentInfo(request.POST)
        if (form1.is_valid and form2.is_valid and form3.is_valid):
            form1.full_clean()
            form2.full_clean()
            form3.full_clean()
            print(form1.cleaned_data)
            print(request.POST)
            # parent_name = request.POST["surname"]
            # child = request.POST["firstName"]
            # # age = request.POST["age"]
            # # child_class = request.POST["child_class"]
            # print(parent_name, child)
            # return HttpResponseRedirect(reverse(request, 'core/homepage'))
            return render(request, 'core/home.html', {'message':'Form submitted successfully'})
        else:
            return render(request, 'core/admission.html', {"form1":form1, "form2":form2, "form3":form3})
    else:
        return render(request, 'core/admission.html', {"form1":forms.CandidateInfo, "form2":forms.CandidatePreviousSchool, "form3":forms.ParentInfo})

class MissionVisionView(TemplateView):
    template_name = 'core/mission_vision.html'

class GalleryView(TemplateView):
    template_name = 'core/gallery.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        images = UpdateImage.objects.filter(published=True).exclude(img_use=2)
        context['images'] = images
        media_url = settings.MEDIA_URL
        context['media_url'] = media_url.replace('/', '')
        context['image_type'] = 1
        return context

class NewsView(TemplateView):
    template_name = 'core/news.html'

class AlumniView(TemplateView):
    template_name = 'core/alumni.html'

class ResourcesView(TemplateView):
    template_name = 'core/resources.html'

class AcademicView(TemplateView):
    template_name = 'core/academics.html'

class StudentView(generic.DetailView):
    template_name = 'core/student.html'
    model = Student

class FacilityView(TemplateView):
    template_name = 'core/facilities.html'

class StaffView(generic.DetailView):
    model = Teacher
    template_name = 'core/staff.html'

    def get_queryset(self):
        return Teacher.objects.filter()

def create_pairs(lst):
    pairs = []
    for i in range(0, len(lst), 2):
        if i+1 < len(lst):
            pairs.append((lst[i], lst[i+1]))
        else:
            pairs.append((lst[i], None))  # Handling odd length lists
    return pairs