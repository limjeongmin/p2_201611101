class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "mt dog name is ",self.name
    def talk(self): 
        print "mung mung" 
         
class ShihtzuDog(Dog): 
    def talk(self): 
        print "si si" 
         
class Maltese(Dog): 
    def talk(self): 
        print "mal mal"
def dogsound():
    mydog1=Dog('poppy') 
    mydog2=ShihtzuDog('poppy') 
    mydog3=Maltese('poppy') 
    mydog1.talk() 
    mydog2.talk() 
    mydog3.talk()

def lab14():
    dogsound()
def main():
    lab14()

if__main__=="__main__":
    main()