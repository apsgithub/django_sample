from django.contrib import admin
from userapp.models import User
from userapp.forms_py import UserForm

# Register your models here.
admin.site.register(User)

