from django.urls import path
from . import views

urlpatterns = [    
    path('chats/',views.chat,name='chatscreen'),
    path('chats/<int:chat_id>',views.view,name='view'),
    path('chats/change_view',views.change_view,name='change_view'),
    path('chats/sent',views.sent,name='sent'),
    path('chats/contacts',views.cont_view,name='contact_list'),
]
