from django.test import TestCase
from random import randint, sample, choice, randrange
from faker import Faker
from rest_framework.test import APITestCase, APIRequestFactory
from movielist.models import Movie, Person
from movielist.serializers import MovieSerializer
from showtimes.models import Cinema, Screening
import time



class CinemaTestCase(APITestCase):
    def setUp(self):
        """Populate test database with random data."""
        self.faker = Faker("pl_PL")
        for _ in range(10):
            self._create_fake_cinema()
        for _ in range(10):
            self._create_fake_screening()

    def _fake_cinema_data(self):
        """Generate a dict of movie data
        The format is compatible with serializers (`Person` relations
        represented by names).
        """
        # kina = ("pod Baranami", "Duże", "Małe", "Max", "Czerwone", "Kameralne", "Multi", "Helios", "City", "Uciecha",
        #         "Rodzinne", "Gloria", "Niebieskie", "jeden", "dwa", "trzy", "cztery")
        cinema_data = {
#            "name": "Kino {}".format(choice(kina)),
            "name": "Kino {}".format(self.faker.name()),
            "city": self.faker.address(),
        }

        print(cinema_data["name"])
        return cinema_data
    def _create_fake_cinema(self):
        """Generate new fake movie and save to database."""
        cinema_data = self._fake_cinema_data()
        new_cinema = Cinema.objects.create(**cinema_data)

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
        if month <10:
            month=str(month)
            month="0"+month
        if day <10:
            day=str(day)
            day="0"+day
        if hour <10:
            hour=str(hour)
            hour="0"+hour
        answer= '2018-{}-{} {}:{}'.format(str(month), str(day), str(hour), minute)
        return answer

    def randcinema(self):
        cinemas = Cinema.objects.all()
        cinemaslist = list(cinemas)
        return choice(cinemaslist)

    def randmovie(self):
        movies = Movie.objects.all()
        movieslist = list(movies)
        return choice(movieslist)

    def format_date(self, date):
        newstr=str(date)
        newstr=newstr.replace("T", " ")
        newstr=newstr[:16]
        return newstr

    def _create_fake_screening(self):
        """Generate new fake movie and save to database."""
        new_screening = Screening.objects.create(date=self.fake_date(), cinema= self.randcinema(), movie=self.randmovie())

    def test_post_cinema(self):
        cinemas_before = Cinema.objects.count()
        new_cinema = self._fake_cinema_data()
        response = self.client.post("/cinemas/", new_cinema, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Cinema.objects.count(), cinemas_before + 1)
        for key, val in new_cinema.items():
            self.assertIn(key, response.data)
            if isinstance(val, list):
                # Compare contents regardless of their order
                self.assertCountEqual(response.data[key], val)
            else:
                self.assertEqual(response.data[key], val)
    def test_get_cinema_list(self):
        response = self.client.get("/cinemas/", {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Cinema.objects.count(), len(response.data))
    def test_get_cinema_detail(self):
        response = self.client.get("/cinemas/1/", {}, format='json')
        self.assertEqual(response.status_code, 200)
        for field in ["name", "city", "movies"]:
            self.assertIn(field, response.data)
    def test_delete_cinema(self):
        response = self.client.delete("/cinemas/1/", {}, format='json')
        self.assertEqual(response.status_code, 204)
        cinema_ids = [cinema.id for cinema in Cinema.objects.all()]
        self.assertNotIn(1, cinema_ids)
    def test_update_cinema(self):
        response = self.client.get("/cinemas/1/", {}, format='json')
        cinema_data = response.data
        new_name = "Multikino"
        cinema_data["name"] = new_name
        new_city = "Krakow"
        cinema_data["city"] = new_city
        response = self.client.patch("/cinemas/1/", cinema_data, format='json')
        self.assertEqual(response.status_code, 200)
        cinema_obj = Cinema.objects.get(id=1)
        self.assertEqual(cinema_obj.name, new_name)
        self.assertEqual(cinema_obj.city, new_city)

#screening tests

    def _fake_screening_data(self):
        screening_data = {
            "date": self.fake_date(),
            "movie": self.randmovie().title,
            "cinema": self.randcinema().name
        }
        return screening_data

    def test_post_screening(self):
        screenings_before = Screening.objects.count()
        new_screening = self._fake_screening_data()
        response = self.client.post("/screening/", new_screening, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Screening.objects.count(), screenings_before + 1)
        for key, val in new_screening.items():
            self.assertIn(key, response.data)
            if isinstance(val, list):
                # Compare contents regardless of their order
                self.assertCountEqual(response.data[key], val)
            else:
                if response.data["date"]:
                    self.assertEqual(self.format_date(response.data[key]), val)
                else:
                    self.assertEqual(response.data[key], val)
    def test_get_screening_list(self):
        response = self.client.get("/screening/", {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Screening.objects.count(), len(response.data))
    def test_get_screening_detail(self):
        response = self.client.get("/screening/1/", {}, format='json')
        self.assertEqual(response.status_code, 200)
        for field in ["date", "cinema", "movie"]:
            self.assertIn(field, response.data)
    def test_delete_screening(self):
        response = self.client.delete("/screening/1/", {}, format='json')
        self.assertEqual(response.status_code, 204)
        screening_ids = [screening.id for screening in Screening.objects.all()]
        self.assertNotIn(1, screening_ids)
    def test_update_screening(self):
        response = self.client.get("/screening/1/", {}, format='json')
        screening_data = response.data
        new_date = self.fake_date()
        screening_data["date"] = new_date
        new_cinema = self.randcinema()
        screening_data["cinema"] = new_cinema.name
        new_movie=self.randmovie()
        screening_data["movie"] = new_movie.title
        response = self.client.patch("/screening/1/", screening_data, format='json')
        self.assertEqual(response.status_code, 200)
        screening_obj = Screening.objects.get(id=1)
        self.assertEqual(self.format_date(screening_obj.date), new_date)
        self.assertEqual(screening_obj.cinema.name, new_cinema.name)
        self.assertEqual(screening_obj.movie.title, new_movie.title)



