from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View
from .models import *

class ObjectsMixin(): #Вывод всех элементов
	model 	 = None
	template = None
	search	 = None  #0 - books  1 - users  2 - authors

	def get(self, request):
		search_query = request.GET.get('search', '')

		if search_query: 
			if (self.search == 0):
				obj = self.model.objects.filter(Title__icontains = search_query)
			elif (self.search == 1):
				obj = self.model.objects.filter(Nickname__icontains = search_query)
			elif (self.search == 2):
				obj = self.model.objects.filter(Author__icontains = search_query)
		else:
			obj = self.model.objects.all()

		
		return render(request, self.template, context = { self.model.__name__.lower() : obj })

class ObjectDetailMixin(): #Вывод определенного элемента
	model 	 	= None
	template 	= None
	name_list 	= None

	def get(self, request, Slug):
		obj = get_object_or_404(self.model, Slug = Slug)
		return render(request, self.template, context = { self.name_list : obj })

class ObjectCreateMixin(): #Создание элемента
	form_model 	= None 
	template 	= None
	redirect_ 	= None

	def get(self, request):
		form = self.form_model()
		return render(request, self.template, context = { 'form' : form }) 


	def post(self, request):
		bound_form = self.form_model(request.POST, request.FILES)

		if bound_form.is_valid():
			new_author = bound_form.save()
			return redirect(self.redirect_)

		return render(request, self.template, context = { 'form' : bound_form })

class ObjectUpdateMixin(): #Изменение элементов
	model 		= None
	form_model 	= None
	template 	= None
	name_list 	= None

	def get(self, request, Slug):
		obj = self.model.objects.get(Slug__iexact = Slug)
		bound_form = self.form_model(instance = obj)
		return render(request, self.template, context = { 'form' : bound_form, self.name_list : obj })

	def post(self, request, Slug):
		obj = self.model.objects.get(Slug__iexact = Slug)
		bound_form = self.form_model(request.POST, request.FILES , instance = obj)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)

		return render(request, self.template, context = { 'form' : bound_form, self.name_list : obj })


class ObjectDeleteMixin(): #Удаление элементов
	model  		= None
	template 	= None
	redirect_ 	= None
	name_list 	= None

	def get(self, request, Slug):
		obj = self.model.objects.get(Slug__iexact = Slug)
		return render(request, self.template, context = { self.name_list : obj })

	def post(self, request, Slug):
		obj = self.model.objects.get(Slug__iexact = Slug)
		obj.delete()
		return redirect(reverse(self.redirect_))