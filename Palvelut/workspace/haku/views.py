from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from datetime import datetime, timedelta, tzinfo
from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import searchForm
from models import Search
from django.db import models
# Create your views here.

def index(request):
    searchform = searchForm()
    template = loader.get_template('haku/index.html')
    context = RequestContext(request, {'form': searchform})

    return HttpResponse(template.render(context))
    
def kartta(request):
    dbhaku = Search.objects.order_by('-date')[0]
    dbvar1 = dbhaku.user
    dbvar2 = dbhaku.service
    dbvar3 = dbhaku.radius
    return render(request, 'haku/kartta.html', {'dbvar1' : dbvar1, 'dbvar2' : dbvar2, 'dbvar3' : dbvar3})
    
def search_new(request):
    if request.method == "POST":
        form = searchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/haku/kartta')
        else:
            raise Http404
    else:
        raise Http404
        
def historia(request):
    dball = Search.objects.order_by('-date')
    dbuser = []
    dbserv = []
    dbrad = []
    for x in range(0, len(dbuser)):
        dbuser [x] = dball.user
        dbserv [x] = dball.service
        dbrad [x] = dball.radius
    return render(request, 'haku/historia.html', {'dbuser' : dbuser, 'dbserv' : dbserv, 'dbrad' : dbrad})
    