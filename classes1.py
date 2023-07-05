#classes & objects

#classes have attributes

class Student:
    srn=0
    name='noname'
    stu_class='noclass'
    electives=[]

    def __init__(self,name,srn,stu_class):
        self.srn=srn
        self.name=name
        self.stu_class=stu_class

    @classmethod
    def person_type(cls):
        print(f"person type is {cls.p_type}")
        print(f"person type is {cls.p_type}")


    def add_electives(self,subject):
        self.electives.append(subject)
s=Student('ram',1234,"2.1")
print()




#methods (class function)-class methids,static method,instane method
#__init__ is used to initialize attributes
# instance method=has access to all the attributes and methods
# class method=can only access class attributes and other class methods
#static method=dosnt have access to the class attributes or other class/instance methods
#The self keyword represents the instance of a class and binds the attributes with the given arguments


#instance method
def func_a(self,b,c,d):
    b=self.a
    print()
    return b