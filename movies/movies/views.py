from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import HttpResponse, render

from .models import Movie


def movies(request):
	# return HttpResponse(data)
	data = Movie.objects.all()
	return render(request, 'movies/movies.html', {'movies': data})

# def api(request):
# 	return HttpResponse("Hello there")

def home(request):
	return HttpResponse("Home page ")

def detail(request, id):
	data = Movie.objects.get(pk=id)
	return render(request, 'movies/detail.html', {'movie': data})

def add(request):
	title = request.POST.get('title')
	year = request.POST.get('year')

	if title and year:
		movie=Movie(title=title, year=year)
		movie.save()
		return HttpResponseRedirect('/movies/')
	return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/movies')
