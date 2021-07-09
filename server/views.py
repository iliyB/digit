from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json
from django.http import *
from .models import *
from .utils import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



#for Table Books

class catalog(ObjectsMixin, View):
	model 	 	= Books
	template 	='blog/catalog.html'
	search 		= 0

class book_detail(ObjectDetailMixin, View):
	model 		= Books
	template	= 'blog/catalog_detail.html'
	name_list 	= 'book'

class book_create(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model 	= FormBooks
	template 	= 'blog/book_create.html'
	redirect_	= '/digit/catalog/'
	raise_exception = True

class book_update(LoginRequiredMixin, ObjectUpdateMixin, View):
	model 		= Books
	form_model	= FormBooks
	template 	= 'blog/book_update.html'
	name_list 	= 'book'
	raise_exception = True

class book_delete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model 		= Books
	template 	= 'blog/book_delete.html'
	redirect_ 	= 'catalog_url'
	name_list	= 'book'
	raise_exception = True

#for Table Users

class users(LoginRequiredMixin, ObjectsMixin, View):
	model 	 	= Users
	template 	= 'blog/users.html'
	search 		= 1
	raise_exception = True

class user_detail(LoginRequiredMixin, ObjectDetailMixin, View):
	model 	 	= Users
	template 	= 'blog/user_detail.html'
	name_list 	= 'user'
	raise_exception = True


class user_create(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model 	= FormUsers
	template 	= 'blog/user_create.html'
	redirect_ 	= '/digit/users/'
	raise_exception = True

class user_update(LoginRequiredMixin, ObjectUpdateMixin, View):
	model 		= Users
	form_model 	= FormUsers
	template 	= 'blog/user_update.html'
	name_list	= 'user'
	raise_exception = True

class user_delete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model 		= Users
	template 	= 'blog/user_delete.html'
	redirect_ 	= 'users_url'
	name_list 	= 'user'
	raise_exception = True

#for Table Authors

class authors(ObjectsMixin, View):
	model 	 	= Authors
	template 	= 'blog/authors.html'
	search		= 2


class author_create(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model 	= FormAuthors
	template	= 'blog/author_create.html'
	redirect_	= '/digit/authors/'
	raise_exception = True

class author_update(LoginRequiredMixin, ObjectUpdateMixin, View):
	model 		= Authors
	form_model 	= FormAuthors
	template 	= 'blog/author_update.html'
	name_list	= 'author'
	raise_exception = True

class author_delete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model 		= Authors
	template 	= 'blog/author_delete.html'
	redirect_ 	= 'authors_url'
	name_list 	= 'author'
	raise_exception = True


	
