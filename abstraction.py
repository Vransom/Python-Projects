from abc import ABC, abstractmethod

class firstdate(ABC): #parent class
    def dinner(self,amount):
        print("Dinner total: ",amount)
    @abstractmethod
    def payment(self,amount):
        pass #passing argument

class moneyinaccount(firstdate): #child class
    #implementing payment function 
    def payment(self,amount):
        print('You have no money in your account and cant pay the {} tab \
                \nThere will be no second date.'.format(amount))

obj=moneyinaccount()
obj.dinner('$50')
obj.payment('$50')
        
