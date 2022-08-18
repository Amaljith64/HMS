from django.shortcuts import render, redirect
from django.contrib import messages
from MyAdmin.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from AccountSection.helpers import*
from django.http import HttpResponse

# Create your views here.


def register(request):
    if request.method == 'POST':

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

            user = Account.objects.create_user(
                username=username,
                password=password1,
                email=email,
                phone_number=phone_number,
            )
            user.save()

# ----------------------OTP REGISTERATION-------------------------

            account_sid = settings.ACCOUNT_SID
            auth_token = settings.AUTH_TOKEN
            client = Client(account_sid, auth_token)

            verification = client.verify \
                .v2 \
                .services(settings.SERVICE_ID) \
                .verifications \
                .create(to=f'{settings.COUNTRY_CODE}{phone_number}', channel='sms')

            print(verification.status)
            return redirect(f'otp/{user.id}/')

    return render(request, "AccountSection/user-register.html")


'''-------------------OTP VERIFICATION--------------------'''


def otpcode(request, id):
    if request.method == 'POST':
        user = Account.objects.get(id=id)
        phone_number = user.phone_number
        otpvalue = request.POST.get('otp')
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
            .v2 \
            .services(settings.SERVICE_ID) \
            .verification_checks \
            .create(to=f'{settings.COUNTRY_CODE}{phone_number}', code=otpvalue)

        print(verification_check.status)
        if verification_check.status=='approved':
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "Wrong otp")
            

    return render(request, 'AccountSection/otp.html')


def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if password == "":
            if Account.objects.filter(username=username):

                phone = Account.objects.get(
                    username=request.POST.get('username'))
                phone_number = phone.phone_number

# ----------------------OTP SIGNIN-------------------------

                account_sid = settings.ACCOUNT_SID
                auth_token = settings.AUTH_TOKEN
                client = Client(account_sid, auth_token)

                verification = client.verify \
                    .v2 \
                    .services(settings.SERVICE_ID) \
                    .verifications \
                    .create(to=f'{settings.COUNTRY_CODE}{phone_number}', channel='sms')
                print(verification.status)
                return redirect(f'otp/{phone.id}/')
            else:
                messages.error(request, "You are not Registered Please Register")

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


def test(request):

    return render(request, 'test.html')


def home(request):
    return render(request, 'AccountSection/homepage.html')


def logout(request):
    auth.logout(request)
    return redirect(signin)
