from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def sign(request):
    return HttpResponse("Hi friend")
