from django.shortcuts import render,redirect
from result.models import *
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from result.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context = {
        'sta':State.objects.all(),
    }
    return render(request,'base.html',context)

def board(request,slug):
    context = {
        'sta':Board.objects.filter(state__slug=slug),
    }
    return render(request,'board.html',context)

def course(request,slug):
    context = {
        'cou':Course.objects.filter(board__slug=slug)
    }
    return render(request,'course.html',context)

def search(request):
    return render(request,'search.html')

def detail(request):
    try:
        if request.method == 'GET':
            search = request.GET.get('search')
            name = request.GET.get('name')
            con = Q(roll_no=search) & Q(name__icontains=name)
            context = {
                'stu':Student_detail.objects.get(con),
            }
    except ObjectDoesNotExist:
        return redirect("search")

    return render(request,'detail.html',context)

def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def admins(request):
    return render(request,'admins/admin.html')

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login( request, user)
            return redirect(admins)

    return render(request,'admins/login.html')

@login_required(login_url='login')
def registerss(request):
    re_form = CreateForm(request.POST or None)
    if request.method == 'POST':
        if re_form.is_valid():
            re_form.save()
            return redirect('login')
    context = {
        'fo':re_form
    }
    return render(request,'admins/register.html',context)

@login_required(login_url='login')
def logouts(request):
    logout(request)
    return redirect(logins)

@login_required(login_url='login')
def add_state(request):
    a_form = Addstate(request.POST or None)
    if request.method == 'POST':
        if a_form.is_valid():
            a_form.save()
            return redirect(admins)
    context = {
        'a_state':a_form
    }
    return render(request,'admins/add_state.html',context)

@login_required(login_url='login')
def add_boards(request):
    b_form = Addboard(request.POST or None)
    if request.method == 'POST':
        if b_form.is_valid():
            b_form.save()
            return redirect(admins)
    context = {
        'bo_add':b_form
    }
    return render(request,'admins/board_add.html',context)

@login_required(login_url='login')
def add_courses(request):
    add_form = Addcourse(request.POST or None)
    if request.method == 'POST':
        if add_form.is_valid():
            add_form.save()
            return redirect("admins")
    context = {
        'ad_course':add_form
    }
    return render(request,'admins/course_add.html',context)

@login_required(login_url='login')
def add_stu_detail(request):
    addd_form = Addstudentdetail(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if addd_form.is_valid():
            addd_form.save()
            return redirect(admins)
    context = {
        'ad_stu_detail':addd_form
    }
    return render(request,'admins/stu_detail_add.html',context)

@login_required(login_url='login')
def view_state(request):
    context = {
        'v_state':State.objects.all()
    }
    return render(request,'admins/view_state.html',context)

@login_required(login_url='login')
def view_board(request):
    context = {
        'v_board':Board.objects.all()
    }
    return render(request,'admins/view_board.html',context)

@login_required(login_url='login')
def view_course(request):
    context = {
        'v_course':Course.objects.all(),
    }
    return render(request,'admins/course_views.html',context)

@login_required(login_url='login')
def view_stu_detail(request):
    context = {
        'v_stu_detail':Student_detail.objects.all()
    }
    return render(request,'admins/view_stu_detail.html',context)