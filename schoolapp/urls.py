"""
URL configuration for schoolapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('adminhome',views.AdminHome.as_view(),name="adminhome"),
    path('studenthome',views.StudentHome.as_view(),name="studenthome"),
    path('register/',views.UserRegistration.as_view(),name="register"),
    path('login/',views.UserLogin.as_view(),name="userlogin"),
    path('logout/',views.UserLogout.as_view(),name="userlogout"),
    path('schoollist/', views.SchoolList.as_view(), name="schoollist"),
    path('addschool/',views.AddSchool.as_view(),name="addschool"),
    path('schooldetails/<int:i>',views.SchoolDetails.as_view(),name="schooldetails"),
    path('studentjoin/<int:i>',views.StudentJoin.as_view(),name="studentjoin"),
    path('leave/<int:i>', views.SchoolLeave.as_view(), name="leave"),

]
