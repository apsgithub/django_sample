from django.shortcuts import render
from django.http import HttpResponse
import userapp
#rom userapp.models import User
from userapp.forms_py  import UserForm

def index(request):
   # mydict ={'insert':'hai from the views file'}
   return render(request,'userapp/home.html')




def userSignUpHtml(request):
    
    formObj = UserForm()
    if request.method == "POST":
        formObj = UserForm(request.POST)
        if formObj.is_valid():
            print("validation success: ")
            print("Name : " +formObj.cleaned_data["fname"])
            formObj.save(commit=True)
            return index(request)
        else:
            print("invalid")
    else:
        print("error")
    return render(request,'userapp/userSignuphtml.html',{'form':formObj})







def userhtml(request):
    user_list = User.objects.all()
    data_dict = {'user_data': user_list}
    return render(request,'userapp/userhtml.html',context=data_dict)


# Create your views here.
