# importing HttResponse from library
from django.http import HttpResponse

def home(request):
    # request is handled using HttpResponse object
    return HttpResponse("Hi! uptimerobot. How are you doing?")