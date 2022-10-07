from django.shortcuts import render, redirect
from django.contrib import messages
from AdminPanel.models import Rooms
from MyAdmin.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from AccountSection.helpers import*
from django.http import HttpResponse
from AdminPanel.models import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from Payments.models import *
from datetime import datetime
from AdminPanel.views import index

# Create your views here.


def register(request):
    referredPerson=None
    code_reffered=None
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        codepattern=username
        referral_code=codepattern.upper()+"REFERRAL"+"500"
        print(referral_code,'referal code')
        if password1 != "":
            if password1 == password2:
                if username == "":
                    messages.error(request, "username is empty")
                    return redirect(register)
                elif Account.objects.filter(username=username):
                    messages.error(request, "username exits")
                    return redirect(register)
                elif Account.objects.filter(email=email):
                    messages.error(request, "email exits")
                    return redirect(register)
                elif email == "":
                    messages.error(request, "email field is empty")
                    return redirect(register)
                elif phone_number == "":
                    messages.error(request, "phone field is empty")
                    return redirect(register)
                

                user = Account.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    phone_number=phone_number,
                )
                
                createdwallet=WalletDetails.objects.create(user=user,amount=0,decription_amount="Wallet Created")
                MyWallet.objects.create(user=user,balance=0,wallet=createdwallet)
                wallet=MyWallet.objects.get(user=user)
                messages.success(request,'Wallet Created')
                try:                   
                    code_reffered=request.POST["referral_code"]
                    referredPerson=Account.objects.get(referral_code__iexact=code_reffered)
                    if referredPerson != None:
                        try:
                            wallet_balance_add=MyWallet.objects.get(user=referredPerson)
                            wallet_balance_add.balance+=500   
                            wallet_balance_add.save()
                            getwallet=WalletDetails.objects.create(user=referredPerson)
                            getwallet.user=referredPerson
                            getwallet.amount=500
                            getwallet.status=True      

                            getwallet.decription_amount="Referral Bonus Credited"
                            getwallet.save()
                            user.ref_active=True
                            print('credited to wallet')
                            messages.success(request,'Refferral applied')
                            createdwallet=WalletDetails.objects.create(user=user,amount=500,decription_amount="Referral Bonus")
                            wallet.balance=500
                            wallet.save()                           
                        except:
                            pass
                    else:
                        messages.error(request,"enter the correct refferral code")
                except:
                    pass
                

                user.code_reffered=code_reffered
                user.referral_code=referral_code
                
                user.save()
                

# ----------------------OTP REGISTERATION-------------------------#

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
            else:
                
                messages.error(request, "Password Not match")
                return redirect(register)
        else:
            messages.error(request, "please fill all fields")
            return redirect(register)

        

    return render(request, "AccountSection/user-register.html")


'''-------------------OTP VERIFICATION--------------------'''


def otpcode(request, id):
    if request.method == 'POST':
        user = Account.objects.get(id=id)
        phone_number = user.phone_number
        otpvalue = request.POST.get('otp')
        if request.POST.get('otp')=="":
            messages.error(request,"please enter otp")
        else:
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
        if username=="":
            messages.error(request, "Invalid Credentials")
            return redirect(signin)

        if password == "":
            if Account.objects.filter(username=username):

                phone = Account.objects.get(
                    username=request.POST.get('username'))
                phone_number = phone.phone_number

# ----------------------OTP SIGNIN-------------------------#

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
            if user.is_superadmin:

            # messages.success(request, 'You have succesfully logged in', )
                return redirect(index)
            else:
                return redirect(home)

        else:
            messages.error(request, "Invalid Credentials")
            print('NOT ABLE TO SIGNIN')
            
    return render(request, 'AccountSection/user-login.html')


def test(request,id):
    order_db = PaymentClass.objects.get(id = id, user = request.user, booked_room__is_booked = True)     #you can filter using order_id as well


    return render(request, 'UserHome/invoice.html',{'details':order_db})



def chech_availability(fd, ed):
        rooms = Rooms.objects.all()
        print('funnnnnnnnnnnnn')
        availableRooms = []
        for room in rooms:
            availList = []
            bookingList = HotelBookings.objects.filter(hotel=room,is_booked=True,start_date__lte=fd,  # less than or equal
                    end_date__gte=ed)
            if len(bookingList) >= room.room_count:
                availList.append(False)
            else:
                availList.append(True)
            if all(availList):
                availableRooms.append(room)
        return availableRooms



def check_booking(start_date, end_date, id, room_count):
    print('Reached Checkinggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
    print(start_date)
    print(end_date)
    print(room_count)
    qs = HotelBookings.objects.filter(
        is_booked=True,
        start_date__lte=start_date,  # less than or equal
        end_date__gte=end_date,  # greater than or equal
        hotel__id=id
    )
    print(qs)
    if len(qs) >= room_count:
        return False
    return True




def home(request):
    rooms=Rooms.objects.all()
    now=date.today()
    coupons=Coupons.objects.filter(valid_to__lte=now)
    request.session['checkin']=None
    request.session['checkout']=None
    scategory_objs = SubCategories.objects.all()

    if request.method == "POST":
        try:
            checkin = request.POST.get("checkin")
            checkout = request.POST.get("checkout")
            
            print(checkin,"uuuuuuuuuuuuuu")

            request.session['checkin']=checkin
            request.session['checkout']=checkout
            
            rooms = chech_availability(checkin, checkout)

            print("hereeeeeeeeeeeeeeee")

            context = {'rooms': rooms,'scategory_objs': scategory_objs}

            return render(request, 'UserHome/allrooms.html', context)
        except:

            messages.error(request, "Choose date")

    for y in coupons:
        y.active=False
        y.save()

    
    for x in rooms:
        list=[]
        # ------------------------ checking for category offer ----------------------- #
        try:
            category_offer=Category_offer.objects.get(category=x.categ,is_active =True)
            list.append(category_offer.discount)
            print(list)
        except ObjectDoesNotExist:
            print('no categoryOffer')
            pass
        # ------------------------ checking for subcategory offer ----------------------- #
        try:
            subcategory_offer=SubCategory_offer.objects.get(subcategory=x.subcateg,is_active =True)
            list.append(subcategory_offer.discount)
            print(list)
        except ObjectDoesNotExist:
            print('no subcategoryOffer')
            pass
        # ------------------------ checking for Room offer ----------------------- #
        try:
            room_offer=Room_offer.objects.get(room=x.id,is_active =True)
            list.append(room_offer.discount)
            print(list)
        except ObjectDoesNotExist:
            print('no roomOffer')
            pass
        #setting discount price zero,if we remove any ofers by chance
        #every time we runserver offers will be set to one again        
        x.discount_price=0
        x.discount_percentage=0
        #incase if there is no any offers for this product(if list is empty) 
        if list:
            maxoffer=max(list)
            print(min(list))
            x.discount_price=x.price-(x.price*maxoffer/100)
            x.discount_percentage=maxoffer
            print(x.discount_price)
            x.save()
        else:
            pass
    return render(request, 'UserHome/index.html',{'rooms':rooms})


def logout(request):
    auth.logout(request)
    return redirect(signin)
