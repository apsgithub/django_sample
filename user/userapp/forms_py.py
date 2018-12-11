# -*- coding: utf-8 -*-
from django.forms import ModelForm
from userapp.models import User


class UserForm(ModelForm):
    class Meta():
        model = User
        fields ='__all__'
