from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		help_texts = {'username':None,'password1':None,'password2':None}
		fields = ("username", "email", "password1", "password2")
        
		# Widget={
		# 	'username':forms.TextInput(attrs={'class':'form-control'}),
		# 	'email':forms.TextInput(attrs={'class':'form-control'}),
		# 	'password1':forms.TextInput(attrs={'class':'form-control'}),
		# 	'password2':forms.TextInput(attrs={'class':'form-control'})
		# }
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user