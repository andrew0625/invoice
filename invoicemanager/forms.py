from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your forms here.

class NewUserForm(UserCreationForm):
	username = forms.CharField(max_length=32)
	organization = forms.CharField(max_length=32)
	first_name = forms.CharField(max_length=32)
	last_name=forms.CharField(max_length=32)
	email=forms.EmailField(max_length=32)
	

	class Meta:
		model = CustomUser
		fields = ("username", "first_name", "last_name", "organization", "email")

	def save(self, commit=True):
		CustomUser = super(NewUserForm, self).save(commit=False)
		CustomUser.email = self.cleaned_data['email']
		if commit:
			CustomUser.save()
		return CustomUser
		
	