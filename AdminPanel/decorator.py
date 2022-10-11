from django.http import HttpResponse


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_superadmin:  
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('you are not authorised to view this page')
    return wrapper_function
