from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def button_index(request):
    context = {}
    return render(request, "button_index.html", context)

def button_email(request):
    context = {}
    send_mail("Kamilka needs love and attention", "Napisz do niej :)", "me@jakub-michalski.tech", ["jakubek.mi@gmail.com"], fail_silently=False,)
    return render(request, "send_email.html", context)
