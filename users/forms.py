from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=["username","email"]
class CustomUserChangeForm(UserChangeForm):
    model=CustomUser
    fields=UserChangeForm.Meta.fields
        
#class RegistrationForm(forms.ModelForm):
#    First_name=forms.CharField(label="First_name")
#    Last_name=forms.CharField(label="Last_name")
#    Password1=forms.CharField(label="Password1")
#    Password2=forms.CharField(label="Password2")
#    class Meta:
#        model=Siteuser
#        fields=("First_name","Last_name","Password1","Password2")

       

#def save(self,commit=True):
#    user = super(RegistrationForm,self).save(commit=True)
 #   user.First_name = cleaned_data["First_name"]
 #   user.Last_name = cleaned_data["Last_name"]
  #  if commit:
  #      user.save()
  #      
  #  return user

