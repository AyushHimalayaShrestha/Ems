from django.shortcuts import redirect
from django.views.decorators.cache import cache_control
def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request, *args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function

# if authenticated
def redirect_if_logged_in(view_func):
    @cache_control(no_cache=True, must_revalidate=True,no_store=True)
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view_func(request,*args,**kwargs)
    return wrapper