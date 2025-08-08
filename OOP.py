class Worker: 
    counter = 0
    
    def __init__(self,name, lastName, salary): # constracters
        self.name = name
        self.lastName = lastName
        self.salary = salary
        self.email = name+lastName+"@gmail.com"
        self.counter = self.counter + 1
    
    def giveNameLastname(self):
        return self.name + " " + self.lastName
    
    def updateSalary(self, raise_rate):
        self.salary = self.salary + self.salary * raise_rate

# worker1 = Worker("Özay", "Yıldız", 200000)
# worker1.name
# worker1.email

# worker1.giveNameLastname()

worker1 = Worker("Ali", "Yıldız", 100)
print("First Salary : " , worker1.salary)
worker1.updateSalary(1.8)
print("First Salary : " , worker1.salary)
 
# %%
l = [lambda x:x**2, lambda x:x+2,lambda x:x*2]
for i in l:
    print(i(5))



