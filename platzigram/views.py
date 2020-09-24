from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Oh, hi !Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %y - %H:%M hrs')
        ))


def sorted_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
            'status': 'ok',
            'numbers': sorted_ints,
            'message': 'integers sorted successfully.',
            }
    return HttpResponse(json.dumps(data, indent=4), content_type='aplication/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'sorry{}, you are not allowed here'.format(name)
    else:
        message = 'sprry{}, you atre not alloweb here'.format(name)
    return HttpResponse(message)
