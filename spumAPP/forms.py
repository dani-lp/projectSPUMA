from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput, label='Password')
	email = forms.EmailField(label='Email', max_length=70)
	first_name = forms.CharField(label='Name', max_length=50)
	last_name = forms.CharField(label='Last name', max_length=50)
	

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput, label='Password')
 
 
class CreateTaskForm(forms.Form):
    title = forms.CharField(label='Content', max_length=50)
    # PRIORITIES = [('low', 'Low'), ('mid', 'Mid'), ('high', 'High')]
    # priority = forms.ChoiceField(choices=PRIORITIES, widget=forms.RadioSelect)