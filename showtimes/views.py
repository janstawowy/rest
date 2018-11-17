from django.shortcuts import render
from showtimes.models import Cinema, Screening
from showtimes.serializers import CinemaSerializer, ScreeningSerializer
from rest_framework import generics
from movielist.models import Movie, Person
from django.db.models import Q
from functools import reduce
from operator import or_


# Create your views here

# All cinemas as a list
class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

#all screenings as a list
class ScreeningListView(generics.ListCreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer

class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer

#screening filtered by movie title passed in an url
class FilteredScreeningListView(generics.ListCreateAPIView):
    serializer_class = ScreeningSerializer
    def get_queryset(self):
        title = self.kwargs['title']
        #get all movies that contain title passed in an url
        movie = Movie.objects.all().filter(title__icontains=title)
        screenings = []
        movies = list(movie)
        #prepare a query for screening that gets all screenings for every movie that match the filter regardless of number of movies that match the criteria
        for movie in movies:
            screenings.append(Q(**{"movie": movie.id}))

        query = reduce(or_, screenings)

        return Screening.objects.filter(query)

#cinemas in a city passed by url
class FilteredCinemaListView(generics.ListCreateAPIView):
    serializer_class = CinemaSerializer
    def get_queryset(self):
        city = self.kwargs['city']
        return Cinema.objects.all().filter(city__icontains=city)






