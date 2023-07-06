import typer
from services.user import UserServices
from models import create_tables

app=typer.Typer()

user_service=UserServices()

@app.command()
def signup(username: str,password: str):
    user_service.signup(username,password)

if __name__ == "__main__":
    create_tables()
    app()
