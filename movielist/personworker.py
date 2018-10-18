from faker import Factory, Faker
from .models import Person


fake = Faker()




def populate_db():

    for i in range (0, 100):
        p=Person()
        p.name=fake.name()
        print(p)
        p.save()



