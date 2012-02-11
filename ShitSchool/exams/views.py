# Create your views here.
from ShitShcool.exams.models import *
from django.shortcuts import *

def home(request):
    return render_to_response("index.html")
