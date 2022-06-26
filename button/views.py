from django.shortcuts import render
from send_notification import send_notification
import random

from button.forms import Form
from button.static_choices import CHOICES

# Create your views here.
def button_index(request):

    if request.method == "POST":
        form = Form(request.POST)
        message = ''
        if request.POST['choice'] == 'other':
            message = request.POST['other']
        else:
            for choice in CHOICES:
                if request.POST['choice'] == choice[0]:
                    message = choice[1]
        # send_mail(what_she_needs, "Napisz do niej :)", "me@jakub-michalski.tech", ["jakubek.mi@gmail.com"], fail_silently=False,)
        send_notification("Wiadomość od...", message, 'a')
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

# show the algorithm with all its properties and provide input form
def algorithms_detail(request, pk):
    algorithm = Algorithm.objects.get(pk=pk)
    if request.method == "POST":
        form = Form(request.POST)
        # case: user choice
        if request.POST['choice'] == 'csv':
            if 'file' in request.POST:
                dataInput='No csv file selected'
            else:
                try:
                    # if it's a csv file, decode the binary file into a text encoding
                    f = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
                    dataInput = csvInput(f)
                except:
                    dataInput = 'Invalid csv file selected. Could not decode.'
        elif request.POST['choice'] == 'own':
            if request.POST['description'] == '':
                dataInput = 'Empty input'
            else:
                # use regular expressions to clean up user array input
                dataInput = cleanUp(request.POST['description'])
                if not dataInput:
                    dataInput = "Input array contains non-numbers"
                elif algorithm.title == 'Binary search':
                    if dataInput != sorted(dataInput):
                        dataInput = "Provided list is not sorted (binary search doesn't on unsorted lists)"
                elif algorithm.title == 'Binary tree search':
                    dataInput.sort()
        elif request.POST['choice'] == 'random':
            if request.POST['description'] == '':
                dataInput = 'Empty input'
            else:
                # generate random array with user defined parameter
                dataInput = randomArray(request.POST['description'])
                if not dataInput:
                    dataInput = "Invalid syntax; syntax: start, end, number of entries, e.g. -5, 5, 7"
                elif algorithm.title in ('Binary search', 'Binary tree search'):
                    dataInput.sort()
        context = {'algorithm': algorithm}
        if algorithm.purpose == 'Search':
            # if it's a search algorithm, get the target element too
            context['target'] = request.POST['target']
            try:
                context['target'] = int(context['target'])
            except:
                dataInput = 'Target is not an integer'
        # change context and run different view depending on whether an error occured
        if type(dataInput)==str:
            context['error'] = dataInput
            return algorithms_error(request, context)
        else:
            context['data'] = dataInput
            return algorithms_result(request, context)
    else:
        form = Form()
    context = {"algorithm": algorithm, 'form':form}
    return render(request, "algorithms_detail.html", context)
