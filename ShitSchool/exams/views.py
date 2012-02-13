from exams.models import *
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from pprint import pprint
from django.contrib.auth import logout
"""
def index(request):
    title = 'Educator 3000 - Where people learn or die'
    uid = 1 # should come from authentication
    name = request.user.ldap_user.attrs["displayName"][0]
    staff = request.user.is_staff
    exams_results = list(Exam.objects.all())
    user = User.objects.get(id=uid)
    ctx = {'title': title, 'exams_list': exams_results, 'user': user, 'name': name, 'staff': staff }
    return render_to_response('exams/index.html', ctx)
"""
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

def exam_add(request, exam_id):
    """ if request.method == 'GET':
        exams = {"exam": Exam.objects.get(pk=exam_id)}
        return render_to_response("postexam.html",exams)
    else: # POST
    # Process the form """
    form_data = ExamForm(request.POST)
    exam_name = form_data["name"]
    exam_deadline = form_data["deadline"]
    exam_author = request.user.ldap_user.attrs["description"][0] # Skilar kennitolu
    new_exam = form_data.save(commit=False) # Creating an instance, but not saving yet
    new_exam.name = exam_name
    new_exam.deadline = exam_deadline
    new_exam.author = exam_author
    # TODO: save the data...
    new_exam.save()  # Saving the new instance of exam
    form_data.save_m2m() # Saving the many to many data for the form
    HttpResponseRedirect('/exams/')
        # Post-Redirect-Get pattern...
    # endif
                    
