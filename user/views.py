from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
  return render(request, 'home.html', {})
    

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #이미 아이디 있으면 오류처리 
        if User.objects.filter(username=username).exists():
            return render(request,'signup_error.html')
        #비번이 null이 아니면 
        if request.POST['password'] : #create_user 안에 save 내포.
            user = User.objects.create_user(username = username, password=password)
            auth.login(request,user)
            print(User.objects.all())
            return redirect('home')
    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user : #null이 아니면
            auth.login(request,user)
            return redirect('home')
        else : 
            return render(request,'login.html',{'error':'check ur id or password '})
    else:
        return render(request,'login.html')
    
def logout_request(request):
    auth.logout(request)
    return redirect('/')
    return render(request,'login.html')