from django.shortcuts import redirect

def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request, *args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function


def redirect_if_logged_in(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view_func(request,*args,**kwargs)
    return wrapper