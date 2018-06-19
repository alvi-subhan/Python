name=input("enter your name")
age=int(input("enter ur age "))
if age >13:
    gender=input("enter your gender\n M for male and F for female")

class Doctor():
    def __init__(self,name,age,gender=""):
        self.age=age
        self.name=name
        if gender:
            self.gender=gender
        else:   pass
    def checking(self):
        print ("welcome "+self.name +" to alvi medical")
    def gender_patient(self):
        if gender=="m" or gender=="M":
            print ("please proceed to left")
        elif gender=="f" or gender=="F":
            print("go to the left")


d=Doctor("wubhan","75","M")
d.checking()
d.gender_patient()
print(d.name.title())


"""def checking(name,age):
    print ("welcome "+ name +" to alvi medical \nyour age is "+str(age))

checking("subhan",45)"""
        
