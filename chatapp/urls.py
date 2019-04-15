from django.contrib import admin 
from django.urls import path,include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.base,name="Home"),
    path('accounts/',include('accounts.urls')),
    path('messages/',include('msg.urls')),
]
