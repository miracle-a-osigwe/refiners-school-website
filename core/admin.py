from django.contrib import admin
from .models import (
    Student, Subject, Teacher, Class, Result, Section, Home, AboutUs, SchoolVision
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    extra = 0

    list_display = ['id', 'std_class']
    list_filter = ['id']

    fieldsets = [
        (None, {
            'fields': ['id', 'std_class']
        })
    ]

    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['id', 'std_class']
        }),
    ]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            # 'fields': ['id', 'category', 'subjects']
            'fields': ['idx', 'subjects']
        })
    ]

    add_fieldsets = [
        (
            {
                # 'fields': ['id', 'category', 'subjects']
                'fields': ['idx', 'subjects']
            }
        )
    ]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


admin.site.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    extra = 0

    list_display = ['id', 'category']
    list_filter = ['id']

    fieldsets = [
        (None, {
            'fields': ['id', 'category']
        })
    ]
# @admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass

