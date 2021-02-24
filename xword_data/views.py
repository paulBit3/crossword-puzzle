from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from datetime import datetime

from django.views.decorators.csrf import csrf_protect
from  .forms import JoinForm
from django.contrib.auth.models import User


from .models import *



# defining our views


def index(request):
    """ the home page of our xword_data app  """
    return render(request, 'pages/index.html', {})

def drill(request):
    """ the DrillView of our xword_data app  """

def display_xwordanswer(request):
    """ the AnswerView of our xword_data app  """




# users creation
@csrf_protect
def join(request):
    """ we will use it to parse request data """
    if request.method == 'POST':
        form = JoinForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            # user.refresh_from_db()
            user.save()
            return render(request, 'accounts/account_success.html', {})
    else:
        form = JoinForm()
    
    return render(request, "accounts/register.html", {'form': form})