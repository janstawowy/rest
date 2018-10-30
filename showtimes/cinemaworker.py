from faker import Factory, Faker
from random import randrange, choice
from .models import Cinema
from django.views import View



fake = Faker()
class fake_cinemamaker(View):
    def fake_cinema():

        kina = ("pod Baranami", "Duże", "Małe", "Max", "Czerwone", "Kameralne", "Multi", "Helios", "City", "Uciecha",
                "Rodzinne", "Gloria")
        Cinema.objects.create(name="Kino {}".format(choice(kina)), city=fake.address())
        return None

def populate_db():

    for i in range(0, 4):
        fake_cinemamaker.fake_cinema()


