#Lecture 1 contents
#-> comment line
# type() is the keyword which returns type of the object

print(type(5))  #int
print(type(9.0))  #Float
print(type(False))  #Bool

#Conversion of one type to another is called casting

print(type(float(5)))  #convert int to float
print(type(int(9.29)))  #convert float to int
print(type(round(3.5)))  #convert float to int by rounding off

#Expression has value and type

print(5/2) # O/P is 2.5
print(type(5/2)) # O/P is float

#assigning values to variables
a=5
print(a)  #O/P is 5

#Variable is bound to one value at a time
a=25
print(a)   #Now O/P is 25

meters = 100   # value of meters is 100
feet = 3.2808*meters   #here the value of meters is 100 and that of feet is 328.08
meters = 200   #meters is rebound to value 200


#Program to swap values of variables
a=5
b=10
print(a,b)   #O/P is 5 10
#The initial values of a and b are 5 and 10 respectively

temp = a
a = b
b = temp
print(a,b) # O/P is 10 5 i.e, values have been swaped using a third variable.

#best method to write a program is giving a meaningfull variable name
pi=3.14
radius=5
area=pi*(radius**2)  #instead of using a and b like dummy variables meaningfull variable names are given

