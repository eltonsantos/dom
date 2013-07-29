#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from launch.views import LaunchSignUpView

urlpatterns = patterns('',
    url(r'^$', LaunchSignUpView.as_view(), name='index'),
)
