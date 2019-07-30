from django import forms
from django.contrib.auth.models import User
from .models import profileModel,aboutResearch,contact

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = profileModel
        fields =['mobile','select',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 400)
    password = forms.CharField(widget =forms.PasswordInput)



class aboutResearchForm(forms.ModelForm):
    
    class Meta:
        model = aboutResearch
        fields = ['subject','about']

class rateingForm(forms.Form):
    rate = forms.IntegerField(max_value=10)

class contactForm(forms.ModelForm):
    class Meta :
        model = contact
        fields = ['email','body']