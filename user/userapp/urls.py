from django.conf.urls import url
from userapp import views
# -*- coding: utf-8 -*-

urlpatterns = [
        url(r'^$',views.userSignUpHtml,name='usersignup'),
  #      url(r'^$',views.userhtml,name='userhtml'),
        ]

