
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about, name='about'),
    
    path('product/', include('product.urls')),  # Include product URLs
    path('dashboard/',include('adminpage.urls')), #Include add category url adminpage
    path('users/',include('users.urls')), # Include user registration URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    