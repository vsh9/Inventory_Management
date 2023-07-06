from models import User

class UserServices:
    def signup(self,username: str, password: str):
        user=User.create(username=username,password=password)
        print(f"{user.username} signed up!")

