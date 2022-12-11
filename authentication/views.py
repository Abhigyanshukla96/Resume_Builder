import json
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

# Create your views here.
def auth(request):
    return render(request, "auth.html")

@csrf_exempt
def login(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            username = data.get("username")
            password = data.get("password")
            
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User logged in successfully")
                django_login(request, user)
                return JsonResponse({'status':'success', 'message':'Login successful','error':False}, status=200)
            
            return JsonResponse({'status':'failed', 'message':'Username/password mismatch. Please try again', 'error':True}, status=403)
    except Exception as e:
        print("Error occured while login: ",e)
        return JsonResponse({'status':'failed', 'message':'Something weird happened. Please try again after sometime', 'error':True}, status=500)
    
@csrf_exempt
def signup(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            
            try:
                user = User.objects.create_user(username, password)
            except:
                return JsonResponse({'status':'failed', 'message':'Username/password already exists. Please try signing up with different username/password.', 'error':True}, status=403)
            
            django_login(request, user)
            return JsonResponse({'status':'success', 'message':'Signed in successful','error':False}, status=200)
    except Exception as e:
        print("Error occured while signing up: ",e)
        return JsonResponse({'status':'failed', 'message':'Something weird happened. Please try again after sometime', 'error':True}, status=500)
        