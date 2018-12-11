from django.shortcuts import render
from . import forms_py
# Create your views here.

def index(request):
    return render(request,'basicformsapp/index.html')
    
def FormPageView(request):
    formObj = forms_py.FormClass()
    
    if request.method == "POST":
        formObj = forms_py.FormClass(request.POST)
        
        if formObj.is_valid():
            print("validation success")
            
            print('Name : ' + formObj.cleaned_data['name'])
            print('Email : '+ formObj.cleaned_data['email'])
            print('Details: '+ formObj.cleaned_data['textarea'])
            #nm=formObj.cleaned_data['name']
            #em1=formObj.cleaned_data['email']
            #dt=formObj.cleaned_data['textarea']
    return render(request,'basicformsapp/forms_page.html',{'form':formObj})
  