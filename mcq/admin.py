from django.contrib import admin


from .models import Question, Option, Answer, Assessment

# Register your models here.

# @admin.register(Option)
class OptionAdmin(admin.StackedInline):
    model = Option
    extra = 4

# @admin.register(Answer)
class AnswerAdmin(admin.TabularInline):
    model = Answer
    extra = 1

# @admin.register(Question)
class QuestionAdmin(admin.StackedInline):
    model = Question
    extra = 1

    # list_display = ['question']
    # list_filter = ['question']

    fieldsets = [
        (None, {
            'fields': ['assessment', 'question', 'upload']}),
    ]

    add_fieldsets = [
        (None, {
            'classes':('wide',),
            'fields': ('assessment', 'question', 'upload'),
        }),
    ]

    inlines = [OptionAdmin, AnswerAdmin]
    filter_vertical = []

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'title', 'author', 'subject', 'class_owner'],
        }),
    ]

    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields':('title', 'author', 'subject', 'class_owner'),
        }),
    ]
    inlines = [QuestionAdmin]