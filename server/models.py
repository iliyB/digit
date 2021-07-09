from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from .validators import *
# Create your models here.

def generate_slug(slug):
	new_slug = slugify(slug, allow_unicode = True)
	return new_slug + '-' + str(int(time()))


class Users(models.Model):
	Id_user 	= models.AutoField(primary_key = True)
	Nickname 	= models.CharField(max_length = 20, unique = True)
	Password 	= models.CharField(max_length = 64)
	Device 		= models.CharField(max_length = 100, db_index = True)
	Name 		= models.CharField(max_length = 20)
	Money 		= models.IntegerField()
	Books 		= models.ManyToManyField('Books', blank = True, related_name = 'users')
	Slug 		= models.SlugField(max_length = 20, unique = True, blank = True)


	def __str__(self):
		return self.Nickname

	def get_absolute_url(self):
		return reverse('user_detail_url', kwargs = {'Slug':self.Slug})

	def get_update_url(self):
		return reverse('user_update_url', kwargs = {'Slug':self.Slug})

	def get_delete_url(self):
		return reverse('user_delete_url', kwargs = {'Slug':self.Slug})

	def save(self, *args, **kwargs):
		if not self.Id_user:
			self.Slug = generate_slug(self.Nickname)
		super().save(*args, **kwargs)


class Books(models.Model):
	Id_book		= models.AutoField(primary_key = True)
	Title 		= models.CharField(max_length = 60)
	Body 		= models.TextField(blank = True, db_index = True)
	Picture 	= models.ImageField(
									validators = [validate_picture], 
									upload_to = 'pictures/'
									)
	File 		= models.FileField(
									blank = True, 
									validators = [validate_file],
									upload_to = 'files/'
									)
	Authors		= models.ManyToManyField('Authors', related_name = 'books')
	Cost 		= models.IntegerField()
	Slug		= models.SlugField(max_length = 30, unique = True, blank = True)

	def __str__(self):
		return self.Title

	def get_absolute_url(self):
		return reverse('catalog_detail_url', kwargs = {'Slug':self.Slug})

	def get_update_url(self):
		return reverse('book_update_url', kwargs = {'Slug':self.Slug})

	def get_delete_url(self):
		return reverse('book_delete_url', kwargs = {'Slug':self.Slug})

	def save(self, *args, **kwargs):
		if not self.Id_book:
			self.Slug = generate_slug(self.Title)
		super().save(*args, **kwargs)


class Authors(models.Model):
	Id_author	= models.AutoField(primary_key = True)
	Author 		= models.CharField(max_length = 30, unique = True)
	Slug 		= models.SlugField(max_length = 30, unique = True, blank = True)

	def __str__(self): 
		return self.Author

	def get_absolute_url(self):
		return reverse('authors_url')

	def get_update_url(self):
		return reverse('author_update_url', kwargs = {'Slug':self.Slug})

	def get_delete_url(self):
		return reverse('author_delete_url', kwargs = {'Slug':self.Slug})

	def save(self, *args, **kwargs):
		if not self.Id_author:
			self.Slug = generate_slug(self.Author)
		super().save(*args, **kwargs)