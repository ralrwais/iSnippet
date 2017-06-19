from django.shortcuts import render

# Create your views here.
from users.models import User 

def login(request):
	users = User.objects.all()
	return render(request, 'users/login.html', {
		'login':users 
		})