

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from accounts import views
# from .models import Item

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']

        email=request.POST['email']
    
        password1=request.POST['password1']
        password2=request.POST['password2']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Exists')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, first_name= first_name, last_name= last_name, password=password1,  email=email)
                user.save()
                print("User created")
                return redirect('/')
        else:
             messages.info(request,'Password not matching')
             return redirect('signup')
        return redirect('/')

    else:
        return render(request,'signup.html')



def log_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        
        ad = authenticate(username= "gauri", password="1797")

        if user is not None :
            if user==ad:
                #return render(request,'admin')
                return redirect('list')
                #return render(request,'list.html')
            else:
                login(request,user)
                return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('log_in')

    else:
        return render(request,'log_in.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# def video(request):
#     obj=Item.objects.all()
#     return render(request,'video.html',{'obj':obj})