from exams.models import *
from datetime import datetime
from django.shortcuts import render_to_response

def home(request):
    ojb = {"current_date": datetime.now(), "name": "Daniel"}    
    return render_to_response("index.html", ojb)
