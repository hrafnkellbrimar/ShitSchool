from django.conf.urls.defaults import patterns, include, url
from ShitSchool.exams.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^exams/$', home),
)
