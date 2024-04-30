from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about_us/', views.AboutView.as_view(), name='about'),
    # path('admission/', views.AdmissionView.as_view(), name='admission'),
    path('admission/', views.admission, name='admission'),
    path('academics/', views.AcademicView.as_view(), name='academics'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('alumni/', views.AlumniView.as_view(), name='alumni'),
    path('resources/', views.ResourcesView.as_view(), name='resources'),
    path('staff/', views.StaffView.as_view(), name='staff'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('mission_vision/', views.MissionVisionView.as_view(), name='mission_vision'),
]