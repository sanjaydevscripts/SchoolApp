from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views import View

from app1.forms import SignUpForm,LoginForm,SchoolForm,StudentForm

from app1.models import School,Student




class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            u = request.user
        return render(request, 'home.html')

class AdminHome(View):
    def get(self, request):
        if request.user.is_authenticated:
            u = request.user
        return render(request, 'adminhome.html')

class StudentHome(View):
    def get(self, request):
        if request.user.is_authenticated:
            u = request.user
        return render(request, 'studenthome.html')

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
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})

    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name = form_instance.cleaned_data['username']
            pwd = form_instance.cleaned_data['password']
            user = authenticate(username=name, password=pwd)
            if user and user.is_superuser == True:
                login(request,user)
                return redirect('adminhome')
            elif user and user.is_superuser != True:
                login(request, user)
                return redirect('studenthome')
            else:
                messages.error(request, 'Invalid credential Please Enter a valid username and password')
                return render(request, 'login.html', {'form': form_instance})

class SchoolList(View):
    def get(self,request):
        s=School.objects.all()
        return render(request,'schoollist.html',{'schools':s})

class AddSchool(View):
    def get(self,request):
        form_instance=SchoolForm()
        return render(request,'register.html',{'form':form_instance})

    def post(self,request):
        form_instance = SchoolForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('schoollist')

class SchoolDetails(View):
    def get(self,request,i):
        s=School.objects.get(id=i)
        can_join=True   #assuming current user not joined in any school initially
        is_student=False #assuming current user is not joined particular school
        u=request.user
        try:
            st=Student.objects.get(user=u)#checks whether the current user joined in any school
            can_join=False
            if st.school==s:    #if the user joined in the that specific school
                is_student=True
        except:
            pass

        return render(request,'schooldetails.html',{'school':s,'can_join':can_join,'is_student':is_student})

class StudentJoin(View):
    def get(self,request,i):
        form_instance=StudentForm()
        return render(request,'addstudent.html',{'form':form_instance})
    def post(self,request,i):
        form_instance=StudentForm(request.POST)
        if form_instance.is_valid():
            student=form_instance.save(commit=False)
            u=request.user
            s=School.objects.get(id=i)
            student.user=u
            student.school=s
            student.save()
            return render(request,'studenthome.html')

class SchoolLeave(View):
    def get(self,request,i):
        s=School.objects.get(id=i)
        u=request.user
        try:
            st=Student.objects.get(school=s,user=u)
            st.delete()
        except:
            pass
        return render(request,'studenthome.html')


class UserLogout(View):
    def get(self,request):
        logout(request)
        return render(request,'login.html')