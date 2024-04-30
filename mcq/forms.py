from django import forms
from django.forms import inlineformset_factory as inf

from .models import Assessment, Question, Option, Answer

class AssessmentCreationForm(forms.ModelForm):
    """
    Custom Assessment Creation Form.
    """
    
    class Meta:
        model = Assessment
        fields = ('__all__')
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
        }
        

class QuestionCreationForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('__all__')
        widgets = {
                'question' : forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'cols': 100, 
                        'rows': 5
                    }
                ),
                'options' : forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'cols': 10, 
                        'rows': 5
                    }
                ),
                'correct_answer': forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'cols': 10,
                        'rows': 2
                    }
                ),   
            }
class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols': 100,
                    'rows': 2
                }
            ),
        }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'answer': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols': 50,
                    'rows': 2
                }
            ),
        }

OptionFormSet = inf(
    Question, Option, form=OptionForm, 
    extra=4, can_delete_extra=True
    )
AnswerFormSet = inf(
    Question, Answer, form=AnswerForm,
    extra=1, can_delete_extra=True
)
