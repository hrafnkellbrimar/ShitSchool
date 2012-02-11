from django.conf.urls.defaults import patterns, include, url
from ShitSchool.exams.views import *
from django.db import models
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^exams/$', home),
)
