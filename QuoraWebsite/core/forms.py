from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter {fieldname}'})
            self.fields[fieldname].help_text = ''  # Remove help text
        self.fields['username'].help_text = ''


        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
