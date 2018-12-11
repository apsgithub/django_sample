# -*- coding: utf-8 -*-
from django import forms
from django.core import validators



class FormClass(forms.Form):
    
    def check_for_name(value):
        if value[:2] != 'a_':
            raise forms.ValidationError("Name Should start with a_")
    
    
    name  = forms.CharField(validators=[check_for_name])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    textarea = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    # trapping a hacker modifying the fields
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) >0:
            raise forms.ValidationError("trapped you BOT")
            print(botcatcher)
        return botcatcher
    #custom Validators  
    
    def check_for_name(value): #value tells python that to use the name field value
        if value[:2] != 'a_':
            raise forms.ValidationError("Name Should start with a_")
    
    def clean(self):
        all_clean_data =  super().clean()
        if all_clean_data['email'] != all_clean_data['verify_email'] :
            raise forms.ValidationError("Email should match")