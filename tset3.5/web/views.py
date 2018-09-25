from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from django.urls import reverse
# Create your views here.


def loginw(request):
    if request.method == 'GET':
        return render(request,'indexw.html')