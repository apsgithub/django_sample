# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','user.settings')

import django
django.setup()

from userapp.models import User
from faker import Faker

fakegen = Faker()

def populate(N):
    for entry in range(N):
        name = fakegen.name()
        name = name.split()
        mailid = fakegen.email()
        user  = User.objects.get_or_create(fname = name[0],lname = name[1],email = mailid )[0]
        
if __name__ =='__main__':
    print("populating.....")
    populate(15)
    print("successfully Populated")

