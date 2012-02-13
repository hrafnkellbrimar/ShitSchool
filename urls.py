from django.conf.urls.defaults import patterns, include, url
from ShitSchool.exams.views import *
from django.db import models
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^exams/$', home),
    (r'^$', home),
    (r'^exams/home/$', home),
    (r'^exams/postexam/$', exam_add),
    (r'^exams/view_exam/$', view_exam),
    (r'^accounts/$','django.contrib.auth.views.login'),
    (r'^accounts/login/$','django.contrib.auth.views.login'),
    (r'^accounts/logout/$','django.contrib.auth.views.logout'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
