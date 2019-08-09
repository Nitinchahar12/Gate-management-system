from django.shortcuts import render
from django.views.generic import CreateView
from .models import Entry_Exit
from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def Entry_Exit_view(request):
    if request.method == 'POST':
        today = datetime.datetime.now().time()
        request.POST.get(today)
        return HttpResponse(request, "entryexit.html")
    else :
        request.method == 'GET'
        a = Entry_Exit.objects.all()
        today = datetime.datetime.now().time()

        return render(request, "entryexit.html", {'qs': a, "today" : today})
