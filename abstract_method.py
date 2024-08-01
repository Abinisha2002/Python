#abstract method
'''from abc import ABC, abstractmethod
class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        "abstract method"
        pass
class SBI(bank):
    def interest(self):
        print("5 percentage")
s=SBI()
s.bank_info()
s.interest()'''
