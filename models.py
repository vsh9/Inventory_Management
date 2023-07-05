#SHOPYOO-THE IMAGINARY SHOPPING MALL
from peewee import *
#database connection
db=SqliteDatabase("shopyoo.db")

class Inventory(Model):
    name=CharField(unique=True)
    price=IntegerField()
    quantity=IntegerField()

    class Meta:
        database=db

def create_tables():
    #create tables in sqlite db
    with db:
        db.create_tables([Inventory])
