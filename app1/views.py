from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views import View

from app1.forms import SignUpForm


class Home(View):
    def get(self,request):
        return render(request,'home.html')


class UserRegistration(View):
    def get(self,request):
        form_instance=SignUpForm()
        return render(request,'register.html',{'form':form_instance})

    def post(self,request):
        form_instance = SignUpForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')

class UserLogin(View):
    def get(self,request):
        return render(request,'login.html')

class UserLogout(View):
    def get(self,request):
        logout(request)
        return render(request,'login.html')