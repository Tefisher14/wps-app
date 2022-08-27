from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return render(request, 'accounts/dashboard.html')


def surveys(request):
    # return HttpResponse('surveys')
    return render(request, 'accounts/surveys.html')


def users(request):
    return render(request, 'accounts/users.html')
