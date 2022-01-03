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


class CreateDashboardForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)


class EditDashboardForm(forms.Form):
    title = forms.CharField(label='Change title', max_length=50)


class CreateTaskForm(forms.Form):
    title = forms.CharField(label='Content', max_length=50)


class CreateNotesForm(forms.Form):
    create_title = forms.CharField(label='Title', max_length=50)
    create_content = forms.CharField(label= 'Content', max_length=500)


class EditNotesForm(forms.Form):
	edit_title = forms.CharField(label='Title', max_length=50)
	edit_content = forms.CharField(label= 'Content', max_length=500)


class CreateHabitsForm(forms.Form):
	title = forms.CharField(label='Title', max_length=50)
	counter = forms.IntegerField(label='Counter')