from rest_framework import serializers
from movielist.models import Movie, Person
from showtimes.models import Cinema, Screening

class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = ("id", "name", "city", "movies")
