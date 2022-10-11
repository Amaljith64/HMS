from django.http import HttpResponse
from django.shortcuts import render


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_superadmin:  
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'AdminPanel/userblockpage.html')
    return wrapper_function
