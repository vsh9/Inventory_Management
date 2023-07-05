import typer
from models import create_tables, Inventory
app=typer.Typer()

@app.command()
def add(name: str,price:int,quantity:int):
    item=Inventory.create(name=name,price=price,quantity=quantity)
    pass
""""
@app.command()
def goofbye(name:str,formal:bool=False):
    pass
"""
    
if __name__ == "__main__":
    create_tables()
    app()