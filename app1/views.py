from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views import View

from app1.forms import SignUpForm,LoginForm


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            u = request.user
        return render(request, 'Home.html')


class UserRegistration(View):
    def get(self,request):
        form_instance=SignUpForm()
        return render(request,'register.html',{'form':form_instance})

    def post(self,request):
        form_instance = SignUpForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')

from django.contrib import messages
class UserLogin(View):
    def get(self,request):
        form_instance=LoginForm
        return render(request,'login.html',{'form':form_instance})

    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name = form_instance.cleaned_data['username']
            pwd = form_instance.cleaned_data['password']
            user = authenticate(username=name, password=pwd)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credential Please Enter a valid username and password')
                return render(request, 'login.html', {'form': form_instance})

class SchoolList(View):
    def get(self,request):
        return render(request,'schoollist.html')


class UserLogout(View):
    def get(self,request):
        logout(request)
        return render(request,'login.html')