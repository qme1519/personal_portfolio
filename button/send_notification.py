from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64
import os
import random

ID_JAKUB = 24066
ID_KAMILA = 0

# ID: Jakub 24066, Kamila?
def send_notification(title, message, id):
	# with open('/etc/pushsafer_key.txt') as f:
	#     PRIVATE_KEY = f.read().strip()

	# random local image
	image_path = '../static/button/img/' + random.choice(os.listdir('../static/button/img'))
	image = open(image_path, 'rb')
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
		"k" : 'KJbfzUi2l2883WM174ES',
		# "p" : 'data:image/jpeg;base64,'+str(image_base.decode('ascii')),
		}

	if id != ID_JAKUB:
		post_fields['m'] = post_fields['m'] + " Wiesz że kocham cię bardziej??"
		post_fields['a'] = 1 # enable answers
		post_fields['ao'] = 'Tak|Tak|Tak'

	request = Request(url, urlencode(post_fields).encode())
	json = urlopen(request).read().decode()
	print(json)