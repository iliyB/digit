from django import forms
from .models import *
from django.core.exceptions import ValidationError
import hashlib



class FormAuthors(forms.ModelForm):
	#Author 		= forms.CharField(max_length = 30)
	#Slug  			= forms.CharField(max_length = 30) 
	#
	#Author.widget.attrs.update({ 'class' : 'form-control' })
	#Slug.widget.attrs.update({ 'class' : 'form-control' })


	class Meta:
		model = Authors
		fields = ['Author']

		widgets = {
			'Author' : forms.TextInput(attrs = {'class' : 'form-control'})
		}

	def clean_Author(self):
		new_Author = self.cleaned_data['Author']

		if Authors.objects.filter(Author__iexact = new_Author).count():
			raise ValidationError('Такой автор уже существует')

		return new_Author


	#def save(self):
	#	new_author = Authors.objects.create(
	#		Author = self.cleaned_data['Author'],
	#		Slug = self.cleaned_data['Slug']
	#		)
	#	return new_author



class FormUsers(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['Nickname', 'Password', 'Name', 'Money', 'Books']

		widgets = {
			'Nickname' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'Password' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'Name' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'Money' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'Books' : forms.SelectMultiple(attrs = {'class' : 'form-control'}),
		}

	def clean_Password(self):
		new_Password = self.cleaned_data['Password']
		if len(new_Password) == 64:
			return new_Password

		new_Password = hashlib.sha256(new_Password.encode('utf-8')).hexdigest()
		return new_Password
		

	#def clean_Nickname(self):
	#	new_Nickname = self.cleaned_data['Nickname'].lower()
#
#		if Users.objects.filter(Nickname__iexact = new_Nickname).count():
#			raise ValidationError('Пользователь с таким именем уже существует')
##
#		return new_Nickname


class FormBooks(forms.ModelForm):
	class Meta():
		model = Books
		fields = ['Title', 'Body', 'Picture', 'File', 'Authors', 'Cost']

		widgets = {
			'Title' : forms.TextInput(attrs = {'class' : 'form-control'}),
		 	'Body' : forms.Textarea(attrs = {'class' : 'form-control'}),
			'Cost' : forms.NumberInput(attrs = {'class' : 'form-control'}),
			'Authors' : forms.SelectMultiple(attrs = {'class' : 'form-control'}),
			'Picture' : forms.FileInput(attrs = {'class' : 'form-control', 'name' : 'pictures'}),
			'File' : forms.FileInput(attrs = {'class' : 'form-control', 'name' : 'files'}),
		}

	def clean_Picture(self):
		new_Picture = self.cleaned_data['Picture']

		return new_Picture






 


