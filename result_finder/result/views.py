from django.shortcuts import render,redirect
from result.models import *
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

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