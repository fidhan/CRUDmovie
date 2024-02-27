from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"movies/home.html")

# def movies(request):
#     return HttpResponse("love maybe?")
# context = {'movies':['movie1','movie2']}
