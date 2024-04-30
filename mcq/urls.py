from django.views.generic import RedirectView
from django.urls import path, re_path
from . import views

app_name = 'mcq'

urlpatterns = [
    re_path(r'^new/$', views.CreateAssessment.as_view(), name='create'),
    re_path(r'^add/$', views.QuestionCreate.as_view(), name='question'),
    re_path(r'^questions/', views.QuestionList.as_view(), name='list_questions'),
    re_path(r'^update/(?P<pk>[-\w]+)/$', views.QuestionUpdate.as_view(), name='question_update'),
    re_path(r'^delete-option/(?P<pk>[-\w]+)/$', views.delete_option, name='delete_option'),
    re_path(r'^detail/(?P<pk>[-\w]+)/$', views.AssessmentDetail.as_view(), name='assessment'),
    re_path(r'^all/', views.ListAssessment.as_view(), name='list'),
    re_path(r'^home/', views.IndexView.as_view(), name='home')
]