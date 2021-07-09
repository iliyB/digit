from django.urls import path

from .views import *
from .ConnectClient import *


urlpatterns = [
	path('catalog/', catalog.as_view(), name = 'catalog_url'),
	path('users/', users.as_view(), name = 'users_url'),
	path('authors/', authors.as_view(), name = 'authors_url'),
	path('users/create/', user_create.as_view(), name = 'user_create_url'),
	path('catalog/create/', book_create.as_view(), name = 'book_create_url'),
	path('authors/create/', author_create.as_view(), name = 'author_create_url'),
	path('users/<str:Slug>', user_detail.as_view(), name = 'user_detail_url'),
	path('catalog/<str:Slug>/', book_detail.as_view(), name = 'catalog_detail_url'),
	path('authors/<str:Slug>/', author_update.as_view(), name = 'author_update_url'),
	path('catalog/<str:Slug>/update/', book_update.as_view(), name = 'book_update_url'),
	path('users/<str:Slug>/update/', user_update.as_view(), name = 'user_update_url'),
	path('users/<str:Slug>/delete/', user_delete.as_view(), name = 'user_delete_url'),
	path('catalog/<str:Slug>/delete/', book_delete.as_view(), name = 'book_delete_url'),
	path('authors/<str:Slug>/delete/', author_delete.as_view(), name = 'author_delete_url'),
	path('check/ping/', check_connect),
	path('check/registration/', registration),
	path('check/authorization/', authorization),
	path('check/get_book/', send_book),
	path('check/catalog/', send_catalog),
	path('check/buy_book/', buy_book),
	path('check/update/', update),
]


#{% url 'user_detail_url' Nickname=user.Nickname %}s