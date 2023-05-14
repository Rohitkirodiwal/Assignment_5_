# Class
class Student:
    def _init(self,name,_RollNmber):  #private properties
        self._name= name
        self._RollNumber=_RollNmber
        print(f"name  : {self._name} \nrollno : {_RollNmber}")

    def setName(self,name): 
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,Rollnumber):
        self.__RollNumber=Rollnumber
    def getRollNumber(self):
        return self.__RollNumber
obj=Student()
(obj.setName("Rohit "))
(obj.setRollNumber(14))
print((obj.getName()))
print((obj.getRollNumber()))