from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm #add this


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	username = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Username', 'class':'form-control'}))

	lastname = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Last Name', 'class':'form-control'}))

	email = forms.EmailField(widget=forms.EmailInput(attrs=
    {'placeholder':'Enter Email ', 'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=
    {'placeholder':'Enter Password', 'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=
    {'placeholder':'Renter Password', 'class':'form-control'}))

	class Meta:
		model = User
		help_texts = {'username':None,'password1':None,'password2':None}
		fields = ("username",'lastname',"email", "password1", "password2")
        
		
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		lname = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		lname.lastname = self.cleaned_data['lastname']
		if commit:
			user.save()
		return user


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Username', 'class':'form-control'}))

	password = forms.CharField(widget=forms.PasswordInput(attrs=
    {'placeholder':'Enter Password', 'class':'form-control'}))