from rest_framework import serializers
from movielist.models import Movie, Person
from showtimes.models import Cinema, Screening
from movielist.serializers import MovieSerializer


class CinemaSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedIdentityField(view_name="moviedetail", many=True, read_only=True)
    class Meta:
        model = Cinema
        fields = ("id", "name", "city", "movies")

class ScreeningSerializer(serializers.HyperlinkedModelSerializer):
    movie=serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all() )
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())
    class Meta:
        model=Screening
        fields=("id", "movie", "date", "cinema")



