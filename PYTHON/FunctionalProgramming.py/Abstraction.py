'''
13-2-25

ABSTRACTION

'''


#abstract class and interface
from abc import ABC,abstractmethod
class Xyz(ABC):
    '''
    Abstract method
         +
    non absratrct or normal method
    '''
    @abstractmethod
    def m1(aelf):       #object creation nhi kiya jata
        pass

    
class RBI(ABC):
    @abstractmethod
    def IFSC_code(self):
        pass
    @abstractmethod
    def CropLoan(self):
        pass


class SBI(RBI):
    def IFSC_code(self):
        return 'SBIN0987'
    def CropLoan(self):
        return 'up to 1 lack'
    def gold_loan():
        return 'Gold'
    

class ATM(ABC):
    AccBalence=600000
    def __init__(self,bal,pin):
        self.bal=bal
        self.pin=pin
    @abstractmethod
    def Withdraw(self):
        pass
    @abstractmethod
    def CheckBalence(self):
        pass


class CBI(ATM):
    def Withdraw(self,amount):
        new_amount = self.bal - amount
        return new_amount
    def CheckBalence(self,amount):
        return self.AccBalence
    def change_pin(self,pin2):
        return (self.pin2)

sbi_card1=CBI(5000,1234)
    
    













