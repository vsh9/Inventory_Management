import typer
from models import create_tables, Inventory
app=typer.Typer()

@app.command()
def add(name: str,price:int,quantity:int):
    item=Inventory.create(name=name,price=price,quantity=quantity)
    pass

@app.command()
def display():
    items=Inventory.select()
    for i in items:
        print(f"{i.name} {i.price} {i.quantity}")


@app.command()
def remove(name: str):
    item=Inventory.get(name=name)
    item.delete_instance()

@app.command()
def goofbye(name:str,formal:bool=False):
    pass

    
if __name__ == "__main__":
    create_tables()
    app()