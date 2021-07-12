from django import forms
from django.contrib.auth.models import User
from .models import Image, Comment, Profile
from django.contrib.auth.forms import UserCreationForm


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption')

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfleUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['profile_image']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']