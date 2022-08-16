from django.shortcuts import render,redirect
from django.contrib import messages
from MyAdmin.models import *
from .models import *
import random
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from AccountSection.helpers import*
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'POST':
        mobile      = '9388816916'
        username = request.POST["username"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if username == "":
                messages.error(request, "username is empty")
                return redirect(register)
            elif Account.objects.filter(username=username):
                messages.error(request, "username exits")
                return redirect(register)
            elif email == "":
                messages.error(request, "email field is empty")
                return redirect(register)
        if mobile == phone_number:
            user = Account.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    phone_number=phone_number,
            )
            user.save()
            account_sid     = settings.ACCOUNT_SID
            auth_token      = settings.AUTH_TOKEN

            client      = Client(account_sid, auth_token)
            global otp
            otp         = str(random.randint(1000, 9999))
            message     = client.messages.create(
                to      ='+919388816916',
                from_    ='+16413296602',
                body    ='Your OTP code is'+ otp)
            messages.success(request, 'OTP has been sent to 9388816916')
            print(otp)
            print('OTP SENT SUCCESSFULLY')
            return redirect(f'otp/{user.id}/')
             
        else:
            messages.info(request, 'Invalid Mobile number')
            return redirect(register)

    return render(request, "AccountSection/user-register.html")


def otpcode(request,id):
    if request.method == 'POST':
        user      = Account.objects.get(id=id)
        otpvalue  = request.POST.get('otp')
        if otpvalue == otp:
            print('VALUE IS EQUAL')
            auth.login(request, user)
            return redirect(home)
        else:
            messages.error(request, 'Invalid OTP')
            print('ERROR ERROR')
            return redirect(otp)

    return render(request,'AccountSection/otp.html')


def signin(request):

   
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)


        if user is not None:
            login(request, user)
        
            messages.success(request, 'You have succesfully logged in', )
            return redirect(home)

        else:
            messages.error(request, "Invalid Credentials")
            print('NOT ABLE TO SIGNIN')
            return HttpResponse("loggedin failed")
    return render(request, 'AccountSection/user-login.html')

def home(request):
    return render(request,'AccountSection/homepage.html')

def logout(request):
    auth.logout(request)
    return redirect(signin)
