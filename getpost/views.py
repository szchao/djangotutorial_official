from django.shortcuts import render
from django.utils import html
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def dumpdata(place, data):
    retval=''
    if len(data) > 0:
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

@csrf_exempt
def failform(request):
    response = """<p>CSRF Fail guessing game...</p>
        <form method="post">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="submit"/>
        </form>"""
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

from django.middleware.csrf import get_token

def csrfform(request):
    response = """<p>CSRF Success guessing game...</p>
        <form method="POST">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="hidden" name="csrfmiddlewaretoken"
            value="__token__"/>
        <input type="submit"/>
        </form>"""

    token = get_token(request)
    print('CSRF from META:', request.META.get('CSRF_COOKIE'))
    print('CSRF from get_token:', token)
    response = response.replace('__token__', html.escape(token))
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

def checkguess(guess) :
    msg = False
    if guess :
        try:
            if int(guess) < 42 :
                msg = 'Guess too low'
            elif int(guess) > 42 :
                msg = 'Guess too high'
            else:
                msg = 'Congratulations!'
        except:
            msg = 'Bad format for guess:' + html.escape(guess)
    return msg

def guess(request):
    guess = request.POST.get('guess')
    print(guess)
    msg = checkguess(guess)
    print('msg:', msg)
    return render(request, 'getpost/guess.html', {'message' : msg })