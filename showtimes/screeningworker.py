from faker import Factory, Faker
from random import randrange, choice
from movielist.models import Movie, Person
from .models import Cinema, Screening
from django.views import View



fake = Faker()
class fake_screeningmaker(View):
    def fake_date(self):
        month=randrange(1,12)
        if month==2:
            day=randrange(1,28)
        elif month % 2 ==0:
            day=randrange(1,30)
        elif month % 2==1:
            day=randrange(1,31)
        hour=randrange(0,23)
        minute=choice(["00","15","30","45"])
        answer= '2018-{}-{} {}:{}'.format(str(month), str(day), str(hour), minute)
        return answer

    def randcinema(self):
        cinemas = Cinema.objects.all()
        cinemaslist=list(cinemas)
        return choice(cinemaslist)
    
    def randmovie(self):
        movies = Movie.objects.all()
        movieslist = list(movies)
        return choice(movieslist)

    def __init__(self):
        Screening.objects.create(cinema=self.randcinema(), movie=self.randmovie(), date=self.fake_date())

        return None




def populate_db():

    for i in range(0, 50):
        fake_screeningmaker()


