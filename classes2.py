class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print(f"Name:,{self.name} | Age:,{self.age} | Gender: {self.gender})
              