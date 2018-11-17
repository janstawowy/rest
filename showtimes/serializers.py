from rest_framework import serializers
from movielist.models import Movie, Person
from showtimes.models import Cinema, Screening
from movielist.serializers import MovieSerializer
import datetime


class CinemaSerializer(serializers.HyperlinkedModelSerializer):

    movies=serializers.SerializerMethodField()


    def get_movies(self, cinema):
        #get screenings that will take place in next 30 days
        screenings=Screening.objects.filter(date__range=[datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=30)] )
        #pass screenings as movies for cinemas containing movie as hyperlink and date of screening
        serializer = CinemaScreeningSerializer(instance= screenings, many=True, read_only=True, context=self.context)
        return serializer.data

    class Meta:
        model = Cinema
        fields = ("id", "name", "city", "movies")

class ScreeningSerializer(serializers.HyperlinkedModelSerializer):
    movie=serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all() )
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())
    class Meta:
        model=Screening
        fields=("id", "movie", "date", "cinema")

class CinemaScreeningSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedIdentityField(view_name="moviedetail", read_only=True)
    class Meta:
        model=Screening
        fields=("movie", "date")



