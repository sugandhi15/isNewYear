import datetime 
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request , 'index.html',{
        "newyear" : now.month == 1 and now.day == 1
    })
