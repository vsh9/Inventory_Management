class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print(f"Name:,{self.name} | Age:,{self.age} | Gender: {self.gender}")

ram=Student("Ram",18,'Male')
ram.info()

student_list=[("StudentM1",19,"Male"), ("StudentM2",20,"Female")]
students=[]
for name,age,gender in student_list:
    s=Student(name,age,gender)
    students.append(s)
    s.info()