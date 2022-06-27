from django.shortcuts import render
import random

from button.forms import Form
from button.static_choices import CHOICES, DESTINATIONS, ID_JAKUB, INDEX_TO_ID

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64
import os
import random

from personalportfolio.settings import BASE_DIR

OTHER_INDEX = 3


# ID: Jakub 24066, Kamila?
def send_notification(title, message, id):
    with open('/etc/pushsafer_key.txt') as f:
	    PRIVATE_KEY = f.read().strip()

	# random local image
    static_path = os.path.join(BASE_DIR, 'static/button/img/')
    image_name = random.choice(os.listdir(static_path))
    image = open(os.path.join(static_path, image_name), 'rb')
    image_read = image.read()
    image_base = base64.encodebytes(image_read)

    url = 'https://www.pushsafer.com/api'
    post_fields = {
		"t" : title,
		"m" : message,
		# "s" : '',
		"v" : 3, # strong vibrations
		"i" : 110, # person with heart icon
		"c" : '#FF0000',
		"d" : 24066,
		"u" : 'https://www.pushsafer.com',
		"ut" : 'Open Pushsafer',
		"k" : PRIVATE_KEY,
		"p" : 'data:image/jpeg;base64,'+str(image_base.decode('ascii')),
		}

    if id != ID_JAKUB:
	    post_fields['m'] = post_fields['m'] + " Wiesz że kocham cię bardziej??"
	    post_fields['a'] = 1 # enable answers
	    post_fields['ao'] = 'Tak|Tak|Tak'

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)

# Create your views here.
def button_index(request):

    if request.method == "POST":
        form = Form(request.POST)

        # determine destination
        destination_index = int(request.POST['destination'])
        destination = INDEX_TO_ID[destination_index]
        source = DESTINATIONS[1 - destination_index][1]
        
        # determine message contents
        message = ''
        index = int(request.POST['choice'])
        if index == OTHER_INDEX:
            message = request.POST['other']
        else:
            message = CHOICES[index][1]
        # send_mail(what_she_needs, "Napisz do niej :)", "me@jakub-michalski.tech", ["jakubek.mi@gmail.com"], fail_silently=False,)
        send_notification("Uwaga!! " + source, message, destination)
        return button_email(request)
    else:
        random_number = random.randint(1,26)
        photo_file_name = "button/img/"+ str(random_number) + ".png"
        form = Form()
        context = {'form':form,
                    'filename': photo_file_name}
    return render(request, "button_index.html", context)

def button_email(request):
    context = {}
    return render(request, "send_email.html", context)