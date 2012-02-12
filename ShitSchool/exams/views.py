from exams.models import *
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    ojb = {"current_date": datetime.now(), "name": "Daniel"}    
    return render_to_response("index.html", ojb) 

def login(request):
    #return render_to_response(r'^accounts/login/$', 'django.contrib.auth.views.login', {'ShitSchool': 'exams/login.html'})
    obj = {"next": "/index.html"}
    return render_to_response("login.html", obj)
