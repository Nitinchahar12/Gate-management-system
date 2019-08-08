from django.shortcuts import render
from django.views.generic import CreateView
from .models import Entry_Exit
from django.shortcuts import render


# Create your views here.
def Entry_Exit_view(request):
    if request.method == 'GET':

        a = Entry_Exit.objects.all()



    return render(request, "entryexit.html", {'qs': a})
