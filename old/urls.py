from django.conf.urls.defaults import patterns, include, url
from ShitSchool.exams.views import *
from django.db import models
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^exams/$', home),
    (r'^exams/home/$', home),
    (r'^exams/postexam/(\d{1})/$', exam_add),
    (r'^exams/view_exam/$', view_exam),
    (r'^accounts/login/$','django.contrib.auth.views.login'),
    (r'^accounts/logout$','django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
)
