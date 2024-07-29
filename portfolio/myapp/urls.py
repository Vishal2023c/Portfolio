from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("data_insert",views.data_insert,name='data_insert'), 
    # path("send_email_to_admin",views.send_email_to_admin,name='send_email_to_admin') ,
]