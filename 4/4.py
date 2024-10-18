class person():
    def __init__(self,name,age,scholarship):
        self.name = name
        self.age = age
        self.scholarship=scholarship
    def print(self):
        print("Name:",self.name,"Age:",self.age,"Scholarship:",self.scholarship())
class student(person):
    def __init__(self,name,age,group_number,avarage):
        self.name=name
        self.age=age
        self.group_number=group_number
        self.avarage=avarage
    def scholarship(self):
        if self.avarage==5:
           print("The scholarship is:",6000,"p")
           return 6000
        if self.avarage <5:
            print("The scholarship is:",4000,"p")
            return 4000
        else:
            print("The scholarship is:",0,"p")
            return 0
    def compare_scholarship(self,others):
        if self.scholarship() == others.scholarship():
            return "equal"
        if self.scholarship() < others.scholarship():
            return "smaller"
        if self.scholarship() > others.scholarship():
            return "larger"
class postgraduate(person):
    def __init__(self,name,age,group_number,avarage,work_title):
        self.name=name
        self.age=age
        self.group_number=group_number
        self.avarage=avarage
        self.work_title=work_title
    def scholarship(self):
        if self.avarage==5:
           print("The scholarship is:",8000,"p")
           return 8000
        if self.avarage <5:
            print("The scholarship is:",6000,"p")
            return 6000
        else:
            print("The scholarship is:",0,"p")
            return 0
    def compare_scholarship(self,others):
        if self.scholarship() == others.scholarship():
            return "equal"
        if self.scholarship() < others.scholarship():
            return "smaller"
        if self.scholarship() > others.scholarship():
            return "larger"

W=student("WQ",12,1,5)
A=postgraduate("AS",22,2,5,"ABC")
print(person.print(W))
print(person.print(A))
print(student.compare_scholarship(W,A))
    
        
