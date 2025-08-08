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

# %%
# List

list_number = [1,2,3,4,5,6]
list_str = ["Monday", "Thourday", "Wednesday"]

type(list_number)

value = list_number[-1]
value

value_last_three = list_number[: 3]
value_last_three

# %%
# List fonctions

list_number = [1,2,3,4,5,6,4,2,7,8]
# list_number.append(7) # .append => sona veri ekler 
# list_number.reverse() # .revorse => ters çevirmekte kullanılır.
list_number.sort()

list_number

# %%
# Tuple

t = (1,2,3,3,4,5,6)
t.count(3)

# %% 
# Dictionary

dictionary = {"ali" : 32, "Ayşe": 34, "Veli": 40}
dictionary.keys()
dictionary.values()
dictionary["Veli"]

# %%
# QUIZZZ

# verilen yılları kaçıncı yüzyıl olduğunu döndüren fonksiyonu yaz

# input = yead >> 1 <= year <= 2005

"""
Year to centuary
"""

def year2Centuary(year):
    str_year = str(year)
    if len(str_year) < 3:
        return 1
    elif len(str_year) == 3:
        if str_year[-2:] == "00":
            return int(str_year[0])
        else:
            return int(str_year[0]) + 1
    else:
        if str_year[2:4] == "00":
            return int(str_year[:2])
        else:
            return int(str_year[:2]) + 1

print(year2Centuary(1881))  # 20

# %%
# Quız

# Bir listeeki en küçük değeri almak istyoruz

my_list = [4,6,8,9,4,63,2,543,6,547,456,435,2,0]
my_list.sort()
my_list[0]
