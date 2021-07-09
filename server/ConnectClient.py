from django.views.decorators.csrf import csrf_exempt
import json
from django.http import *
from .models import *


@csrf_exempt
def check_connect(requset):
	result = {};
	result['code'] = 1000

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code = json_data['code']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 0:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)

	return JsonResponse(result)

@csrf_exempt
def registration(requset):
	result = {}
	result['code'] = 1011

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code 		= json_data['code']
			g_nickname 	= json_data['nickname']
			g_password 	= json_data['password']
			g_name 		= json_data['name']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 11:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)
		else:
			if Users.objects.filter(Nickname__iexact = g_nickname).count():
				result['code'] = 1911
				result['error'] = "Пользователь с таким никнеймом уже существует"
				return JsonResponse(result)
			else:
				user = Users(Nickname = g_nickname, Password = g_password, Name = g_name, Money = 0)
				user.save()
				return JsonResponse(result)


@csrf_exempt
def authorization(requset):
	result = {}
	result['code'] = 1001

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code 		= json_data['code']
			g_device 	= json_data['device']
			g_password 	= json_data['password']
			g_nickname 	= json_data['nickname']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 1:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)
		else:
			if not (Users.objects.filter(Nickname__iexact = g_nickname).filter(Password = g_password).count()):
				result['code'] = 1991
				result['error'] = "Данные не подходят"
				return JsonResponse(result)
			else:
				user = Users.objects.get(Nickname__iexact = g_nickname)
				user.Device = g_device
				user.save()
				books = user.Books.all()
				id_books = [book.Id_book for book in books]
				result['name'] = user.Name
				result['cash'] = user.Money
				result['id'] = user.Id_user
				result['id_books'] = id_books
				return JsonResponse(result)


@csrf_exempt
def send_book(requset):
	result = {}
	result['code'] = 1002

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code 		= json_data['code']
			g_id_book 	= json_data['id_book']
			g_id_user 	= json_data['id_user']
			g_device 	= json_data['device']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 2:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)
		else:
			user = Users.objects.get(Id_user = g_id_user)

			if (user == None):
				result['code'] = 1999
				result['error'] = "Пользователь с таким id отсутствует"
				return JsonResponse(result)
			if (user.Device != g_device):
				result['code'] = 1999
				result['error'] = "Неправильная сессия"
				return JsonResponse(result)

			ok = False

			books = user.Books.all()
			id_books = [book.Id_book for book in books]
			for id_b in id_books:
				if (id_b == g_id_book):
					book = Books.objects.get(Id_book = id_b)
					ok = True
					break

			if ok:
				result['title'] = book.Title
				result['body'] = book.Body
				result['cost'] = book.Cost
				stroka = ""
				for author in book.Authors.all():
					stroka += author.Author + ", "
				result['authors'] = stroka
				return JsonResponse(result)
			else:
				result['code'] = 1999
				result['error'] = "Неправильная книга"
				return JsonResponse(result)


@csrf_exempt
def send_catalog(requset):
	result = {}
	result['code'] = 1003

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code 		= json_data['code']
			g_id_user 	= json_data['id_user']
			g_device 	= json_data['device']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 3:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)
		else:
			user = Users.objects.get(Id_user = g_id_user)

			if (user == None):
				result['code'] = 1999
				result['error'] = "Пользователь с таким id отсутствует"
				return JsonResponse(result)
			if (user.Device != g_device):
				result['code'] = 1999
				result['error'] = "Неправильная сессия"
				return JsonResponse(result)

			books = Books.objects.all()

			id_books 		= []
			title_books 	= []
			body_books 		= []
			authors_books 	= []
			cost_books 		= []

			for book in books:
				id_books.append(book.Id_book)
				title_books.append(book.Title)
				body_books.append(book.Body)
				cost_books.append(book.Cost)
				authors = ""
				for author in book.Authors.all():
					authors += author.Author + ", "
				authors_books.append(authors)

			result['id_books'] 		= id_books
			result['title_books'] 	= title_books
			result['body_books'] 	= body_books
			result['authors_books'] = authors_books
			result['cost_books'] 	= cost_books

			return JsonResponse(result)


@csrf_exempt
def buy_book(requset):
	result = {}
	result['code'] = 1004

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code 		= json_data['code']
			g_id_user 	= json_data['id_user']
			g_id_book 	= json_data['id_book']
			g_device 	= json_data['device']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 4:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)
		else:
			user = Users.objects.get(Id_user = g_id_user)

			if (user == None):
				result['code'] = 1999
				result['error'] = "Пользователь с таким id отсутствует"
				return JsonResponse(result)
			if (user.Device != g_device):
				result['code'] = 1999
				result['error'] = "Неправильная сессия"
				return JsonResponse(result)


			book = Books.objects.get(Id_book = g_id_book)
			
			res = user.Money - book.Cost
			if (res >= 0):
				user.Money = res
				user.Books.add(book)
				user.save()
				result['cash'] = res
				return JsonResponse(result)
			else:
				result['code'] = 1914
				result['cash'] = user.Money
				result['error'] = "Недостаточно средств"
				return JsonResponse(result)


@csrf_exempt
def update(requset):
	result = {}
	result['code'] = 1005

	if requset.method == 'POST':
		json_data = json.loads(requset.body.decode("utf-8"))
		try:
			g_code 		= json_data['code']
			g_device 	= json_data['device']
			g_id_user 	= json_data['id_user']
		except KeyError:
			result['code'] = 1999
			result['error'] = "Ошибка разбора выражения"
			return JsonResponse(result)

		if g_code != 5:
			result['code'] = 1999
			result['error'] = "Неправильный код запроса"
			return JsonResponse(result)
		else:
			user = Users.objects.get(Id_user = g_id_user)

			if (user == None):
				result['code'] = 1999
				result['error'] = "Пользователь с таким id отсутствует"
				return JsonResponse(result)
			if (user.Device != g_device):
				result['code'] = 1999
				result['error'] = "Неправильная сессия"
				return JsonResponse(result)

			result['nickname'] 	= user.Nickname
			result['name'] 		= user.Name
			result['password'] 	= user.Password
			result['cash'] 		= user.Money
			return JsonResponse(result) 
