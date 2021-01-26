"""result_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from result.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('board/<str:slug>/',board,name='boards'),
    path('course/<str:slug>/',course,name='courses'),
    path('search/',search,name='search'),
    path('detail/',detail,name='detail'),
    path('about/',about,name='about'),
    path('admins/login/',logins,name='login'),
    path('logout/',logouts,name='logout'),
    path('admins/signup/',registerss,name='signup'),
    path('admins/add_state/',add_state,name='add_state'),
    path('admins/add_boards',add_boards,name='add-boards'),
    path('admins/add_course/',add_courses,name='add_course'),
    path('admins/add_stu_detail/',add_stu_detail,name='add_stu_detail'),
    path('admins/view_state/',view_state,name='view_state'),
    path('admins/view_board/',view_board,name='view_board'),
    path('admins/view_course/',view_course,name='view_course'),
    path('admins/view_stu_detail/',view_stu_detail,name='view_stu_detail'),
    path('admins/admins/',admins,name='admins'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
