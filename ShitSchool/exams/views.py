from exams.models import *
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from pprint import pprint
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect(ShitSchool.exams.views.login)

@login_required
def home(request):
    #pprint( vars( request.user ) )
    #log.debug("This will be printed to the console")
    ojb = {"current_date": datetime.now(), "name": "Daniel"}    
    return render_to_response("index.html", ojb) 

def login(request):
    #return render_to_response(r'^accounts/login/$', 'django.contrib.auth.views.login', {'ShitSchool': 'exams/login.html'})
    obj = {"next": "/index.html"}
    return render_to_response("login.html", obj)
