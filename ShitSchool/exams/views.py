from exams.models import *
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from pprint import pprint

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

def exams_add(request, exam_id):
    if request.method == 'GET':
        exam = Exam.objects.get(pk=exam_id)
        return render_to_response("exam.html",exam)
    else: # POST
    # Process the form
    endif
    else: # POST
    # Process the form
        form_data = request.POST
        name = form_data["name"]
        # TODO: save the data...
        HttpResponseRedirect('/exams/')
        # Post-Redirect-Get pattern...
    endif
                    
