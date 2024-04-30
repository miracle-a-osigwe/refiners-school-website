from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from .models import (
    Assessment, Question, Option, Answer
)
from .forms import (
    QuestionCreationForm, OptionFormSet, AnswerFormSet
)

User = get_user_model()
# Create your views here.

# set an app name
app_name = 'mcq'

class QuestionInline():
    form_class = QuestionCreationForm
    model = Question
    template_name = 'mcq/question_create_or_update.html'

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        print(named_formsets)
        if not all((val.is_valid() for val in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # Look for specific formset save function and if not found, simply save directly.

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, f'formset_{name}_valid', None)
            if not formset_save_func is None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('mcq:list_questions')
    
    def formset_option_valid(self, formset):
        """
        Custom option formset saving.
        """
        options = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()
        for option in options:
            option.question_tag = self.object
            option.save()
    

    def formset_answer_valid(self, formset):
        """
        Custom answer formset saving
        """
        answer = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()
        
        for ans in answer:
            ans.question_number = self.object
            ans.save()

class QuestionCreate(LoginRequiredMixin, QuestionInline, generic.CreateView):
    def get_context_data(self, **kwargs):
        ctx = super(QuestionCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        print(ctx)
        return ctx
    
    def get_named_formsets(self):
        if self.request.method == 'GET':
            return {
                'option' : OptionFormSet(prefix='option'),
                'answer' : AnswerFormSet(prefix='answer')
            }
        else:
            return {
                'option' : OptionFormSet(self.request.POST or None, self.request.FILES or None, prefix='option'),
                'answer' : AnswerFormSet(self.request.POST or None, self.request.FILES or None, prefix='answer')
            }

class QuestionUpdate(LoginRequiredMixin, QuestionInline, generic.CreateView):
    def get_context_data(self, **kwargs):
        ctx = super(QuestionUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'option': OptionFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='option'),
            'answer': AnswerFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='answer')
        }


class QuestionList(generic.ListView):
    model = Question
    template_name = 'mcq/question_list.html'
    # context_object_name = 'questions'

    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)

class OptionList(generic.ListView):
    model = Option
    context_object_name = 'options'

class AnswerList(generic.ListView):
    model = Answer
    context_object_name = 'answers'

class CreateQuestion(LoginRequiredMixin, generic.CreateView):
    """Create Questions."""
    model = Question
    fields = ('__all__')

    def get(self, request, **kwargs):
        self.object = None
        context_dict = self.get_context_data()
        context_dict.update(user_role=self.request.user.role)
        return self.render_to_response(context_dict)

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(CreateQuestion, self).form_valid(form)


class CreateAssessment(LoginRequiredMixin, generic.CreateView):
    fields = ('__all__')
    model = Assessment

    def get(self, request, **kwargs):
        self.object = None
        context_dict = self.get_context_data()
        context_dict.update(user_role = self.request.user.role)
        return self.render_to_response(context_dict)
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(CreateAssessment, self).form_valid(form)


class IndexView(generic.ListView):
    template_name = 'mcq/home.html'
    model = Assessment

class AssessmentDetail(generic.DetailView):
    model = Assessment
    template_name = 'mcq/assessment_detail.html'

    def get_context_data(self, **kwargs):
        """
        Return the assessments created by the user.
        """
        if 'id' in kwargs.keys():
            self.kwargs['pk'] = kwargs['id']
        
        # response = Assessment.objects.filter(id=self.kwargs['id'])
        question = Question.objects.filter(assessment=self.kwargs['pk'])
        q = Question.objects.values('id', 'assessment_id')
        context = super(AssessmentDetail, self).get_context_data(**kwargs)
        context['question'] = question
        options = []
        answers = []
        if len(question) > 0:
            for val in q:
                if val['assessment_id'] == int(self.kwargs['pk']):
                    opt = []
                    ans = []
                    option = Option.objects.filter(question_tag_id = val['id'])
                    for op in option:
                        opt.append(op)
                    answer = Answer.objects.filter(question_number_id = val['id'])
                    for an in answer:
                        ans.append(an)
                    options.append(option)
                    answers.append(answer)
        context['option'] = options
        context['answer'] = answers
        return context



class ListAssessment(generic.ListView):
    model = Assessment
    template_name = 'assessment_list.html'

class TakeAssessment(generic.ListView):
    pass


def delete_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        messages.success(
            request, 'Object does not exit'
        )
        return redirect('mcq:update_question', pk=option.question_tag.id)
    option.delete()
    messages.success(
        request, 'Option deleted successfully'
    )
    return redirect('mcq:update_question', pk=option.question_tag.id)