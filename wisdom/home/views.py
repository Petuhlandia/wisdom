from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    wordlist = ["Home"]
    template = loader.get_template("home/index.html")
    context = {
        "wordlist": wordlist
    }
    return HttpResponse(template.render(context, request))