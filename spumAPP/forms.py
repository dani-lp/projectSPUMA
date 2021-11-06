from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField(label='Introduce tu nombre', max_length=100)
	tlf = forms.CharField(label='Introduce tu telefono', max_length=100)

	class Meta:
		model = User
		fields = ("username", "password1", "password2","name", "email", "tlf")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.tlf = self.cleaned_data['tlf']

		if commit:
			user.save()
		return user

    


 