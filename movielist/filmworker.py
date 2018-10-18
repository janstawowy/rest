from faker import Factory, Faker
from random import randrange, choice
from .models import Movie, Person
from django.views import View



fake = Faker()
class fake_filmmaker(View):
    def fake_film():
        actors = Person.objects.all()
        actorlist = list(actors)

        t1 = ["Tajemnica", "Śmierć", "Kod", "Zabójstwo", "Śledztwo", "Proces",
              "Gra", "Bogactwo", "Teoria", "Miłość", "Dane", "Szyfry", "Zagadka",
              "Manipulacja", "Szansa", "Żal", "Broń", "Zdrowie", "Herezja",
              "Porwanie", "Poszukiwania", "Zabawa", "Programy", "Pieniądze",
              "Komunikat", "Leczenie", "Psychoterapia", "Rozrywka", "Ból",
              "Dziewczyny", "Chłopaki", "Druhny", "Rodzice", "Dzieci", "Dziadkowie",
              "Narzeczone", "Żony", "Szaleńcy", "Prześladowcy", "Smutek", "Zabawki",
              "Samotność", "Krew"]

        t2 = ["Afrodyty", "Da Vinci", "ucznia", "Newtona", "Einsteina", "rycerza",
              "wojownika", "lęku", "sportowców", "komputerów", "nauki",
              "czarownic", "kierowców", "żołnierzy", "przyrody",
              "dla profesjonalistów", "naukowców", "zwierząt", "w Kosmosie",
              "na bogato", "w Polsce", "w Azji", "w Afryce", "w Europie", "w Ameryce",
              "we współczesnym świecie", "w górach", "nad morzem", "na rynku",
              "w polityce", "Polaków", "Europy", "na wojnie", "dla każdego",
              "w weekend", "w twoim domu", "lekarzy", "królów", "prezydentów",
              "zapomnianych", "Złego", "bogów", "szpiega", "w deszczu",
              "tyrana", "milionerów", "w wielkim mieście", "dla dzieci",
              "w ciemności"]

        m = Movie()
        m.title = "{} {}".format(choice(t1), choice(t2))
        m.description = fake.text()
        m.director = actorlist[randrange(0, len(actorlist))]
        m.year = randrange(1950, 2018)
        m.save()
        for i in range(0, randrange(3, 10)):
            m.actors.add(actorlist[randrange(0, len(actorlist))])
        print(m)
        m.save()
        return None




def populate_db():

    for i in range(0, 100):
        fake_filmmaker.fake_film()


