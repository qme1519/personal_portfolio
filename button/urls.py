from django.urls import path
from . import views

urlpatterns = [
    path("", views.button_index, name="button_index")
]

#    path("send_email", views.button_email, name="button_email")
