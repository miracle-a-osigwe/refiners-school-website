from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Teacher, Student, Home, AboutUs
from . import forms


# Create your views here.

#set app name
app_name = 'core'

class IndexView(TemplateView):
    template_name = 'core/home.html'
    # model = Home

class AboutView(TemplateView):
    template_name = 'core/about.html'

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

class StaffView(generic.DetailView):
    model = Teacher
    template_name = 'core/staff.html'

    def get_queryset(self):
        return Teacher.objects.filter()