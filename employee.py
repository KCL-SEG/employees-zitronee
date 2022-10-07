"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryNoCommission (Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.salary}."



class HourlyNoCommission (Employee):
    def __init__(self, name, hourlyWage, hoursWorked):
        super().__init__(name)
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked

    def get_pay(self):
        return self.hourlyWage * self.hoursWorked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyWage}/hour. Their total pay is {self.get_pay()}."


class SalaryBonus (Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."

class HourlyBonus (Employee):
    def __init__(self, name, hourlyWage, hoursWorked, bonus):
        super().__init__(name)
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked
        self.bonus = bonus

    def get_pay(self):
        return self.hourlyWage * self.hoursWorked + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class SalaryContract (Employee):
    def __init__(self, name, salary, noContract, contractPrice):
        super().__init__(name)
        self.salary = salary
        self.noContract = noContract
        self.contractPrice = contractPrice

    def get_pay(self):
        return self.salary + self.noContract*self.contractPrice

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.noContract} contract(s) at {self.contractPrice}/contract. Their total pay is {self.get_pay()}."


class HourlyContract (Employee):
    def __init__(self, name, hourlyWage, hoursWorked, noContract, contractPrice):
        super().__init__(name)
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked
        self.noContract = noContract
        self.contractPrice = contractPrice

    def get_pay(self):
        return self.hourlyWage * self.hoursWorked + self.noContract*self.contractPrice
    def __str__(self):
        return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyWage}/hour and receives a commission for {self.noContract} contract(s) at {self.contractPrice}/contract. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#billie = Employee('Billie')
billie = SalaryNoCommission('Billie', 4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyNoCommission('Charlie', 25, 100)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContract('Renee',3000, 4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContract('Jan', 25, 150, 3, 220)



# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonus('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyBonus('Ariel', 30, 120, 600)
#ariel = Employee('Ariel')
