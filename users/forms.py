from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	MedicalId = forms.CharField(label='Medical Id', max_length=10)

	class Meta:
		model= User
		fields = ['username', 'email', 'MedicalId', 'password1', 'password2']