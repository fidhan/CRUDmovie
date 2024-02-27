from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from list.models import Movie

# Create your views here.
# context = {
#     'movies': [
#         {
#             'title':'shark',
#             'year':2009,
#             'id':5,
#         },
#                 {
#             'title':'shark2',
#             'year':2005,
#             'id':6,
#         },
#                         {
#             'title':'shark3',
#             'year':2004,
#             'id':4,
#         }
#     ]
# }
def movies(request):
    data = Movie.objects.all()
    print(data)
    print(data)
    context = {
        'movies':data
    }
    return render(request,'movies/movies_list.html',context)


def detail(request,id):
    data = Movie.objects.get(pk=id)
    context = {
        'movies':data
    }
    return render(request,'movies/details.html',context)


def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    

    if title and year:
        movie = Movie(title=title,year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request,'movies/add.html')

def delete(request,id):
    try:
        movie = Movie.objects.get(pk=id)
        
    except:
        raise Http404("movie dies not exist")
    movie.delete()
    return HttpResponseRedirect('/movies')

def update(request, id):
    movie = get_object_or_404(Movie, pk=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        
        if title and year:
            movie.title = title
            movie.year = year
            movie.save()
            return HttpResponseRedirect('/movies')
    
    return render(request, 'movies/update.html', {'movie': movie})