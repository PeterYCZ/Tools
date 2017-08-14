from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
import datetime

def hello(request):
    name = 'Peter'
    return render_to_response('hello.html', {'name':name})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.<p>!!!!</p></body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


