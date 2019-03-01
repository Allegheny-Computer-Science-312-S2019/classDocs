from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1> This is the hello App homepage </h1>")
#Write the return string on a single line.
