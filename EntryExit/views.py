from django.shortcuts import render
from django.views.generic import CreateView
from .models import Entry_Exit
from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def Entry_Exit_view(request):
    if request.method == 'POST':
        request.POST.get('div1')

        return HttpResponse(request, "entryexit.html")
    elif request.method == 'GET':
        a = Entry_Exit.objects.all()
        request.POST.get('div1')
        print("111")

        return render(request, "entryexit.html", {'qs': a,} )
