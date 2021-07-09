from django.shortcuts import redirect

def redirect_digit(request):
	return redirect('catalog_url', permanent = True);