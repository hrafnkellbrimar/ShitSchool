from exams.models import *
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from pprint import pprint
from django.contrib.auth import logout
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseRedirect


def logout(request):
    logout(request)
    # Redirect to a success page.
    return render("logout.html")

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

@csrf_protect
def view_exam(request):
    QuestionFormSet = formset_factory(QuestionForm)
    OptionsFormSet = formset_factory(OptionForm)
    if request.method == 'POST':
        question_formset = QuestionFormSet(request.POST, request.FILES, prefix='question')
        options_formset = OptionsFormSet(request.POST, request.FILES, prefix='options')
        if article_formset.is_valid() and book_formset.is_valid():
            for form in question_formset:
                print form()
            for form in options_formset():
                print form()
            pass
    else:
        question_formset = QuestionFormSet(prefix='question')
        options_formset = OptionsFormSet(prefix='opttions')
    return render_to_response('view_exam.html', {'question_formset': question_formset, 'options_formset': options_formset},context_instance=RequestContext(request))
# Python magic inspired by: http://themorgue.org/blog/2008/05/14/django-and-modelform/ :
@csrf_protect
def exam_add(request, id=None):
    form = ExamForm(request.POST or None,instance=id and Exam.objects.get(id=id))
    # Save exam:
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/exams/view_exam/')
    return render_to_response('postexam.html', {'form':form},context_instance=RequestContext(request))


