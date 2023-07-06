import typer
from models import Inventory,create_tables
from services.inventory import InventoryService
app=typer.Typer()


inventory=InventoryService()


@app.command()
def add(name: str,price:int,quantity:int):
    inventory.add(name=name,price=price,quantity=quantity)
   

@app.command()
def display():
    inventory.display()


@app.command()
def remove(name: str):
    inventory.remove(name)

if __name__ == "__main__":
    create_tables()
    app()
