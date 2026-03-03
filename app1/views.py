from django.shortcuts import render

from django.http import HttpResponse

def gautam(request):
    return HttpResponse ("gautam is a good boy")
def ganesh(request):
    return HttpResponse ("<h1>ganesh is a good boy</h1>")
def chunu(request):
    return HttpResponse ("<h1 style='color:red; '><marquee>chunu is a good girl</marquee></h1>")



