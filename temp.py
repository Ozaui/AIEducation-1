# %%
# User Defiend funcitons

def myFirstFunc(var1, var2):
    """
    This is my first phyton function
    
    parameters:
        
    return:
    """
    output = (((var1 + var2) * 50)/100.0)*var1/var2
    return output
    
myFirstFunc(10, 100)

# %%

def try1():
    print("This is a string")
    
try1()

# %%

# Default and flexable functions
# Default
def calculateCircleEnvironment(r,pi = 3.14):
    """
    calculate circle enviroment
    input(parameter): r,pi
    output : circle enviroment
  
    """
    output = 2*3.14*r
    return output

calculateCircleEnvironment(3)

# Flexable
def calculateBody(height, weight):
    return height + weight

def calculateBody(height,weight,*args):
    print(len(args))
    output =  (height + weight)*args[0]
    return output

calculateBody(10, 1, 5,1,3,4,)

# %% 
# QUIZZZZZZZZ

# int variable age
# string name
# fonc print(type(), len, float())
# *args surname
# default parameter for shoe number

age = 10
name = "Özay"
surname = "Yıldız"

def functionQuiz(age,name,surname, *args, numberofShoe = 35,):
    print("age" + age)
    print("name" + name)
    print("number of Shoe" + numberofShoe)
    print(type(name))
    print(float(age))
    output = args[0] * age
    return output

functionQuiz(age, name, surname)

# %%
def calculateLambda(x):
    output = x*x
    return output
result = calculateLambda(2)
result

result2 = lambda x: x*x
print(result2(4))