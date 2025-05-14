#STRINGS
    #sequence of characters like "apple" , "coke"
    #should be written inside quotations
    #s=2*a this means that output will be aa that is that character "a" is repeated 2 times since 2*a

b=":"
c=")"
s1=b+2*c
print(s1)   #O/P is :))

f="a"
g="b"
h="3"
s2=(f+g)*(int(h))
print(s2)   #O/P is ababab

#len() -> A fn that returns length of string
s="string"
print(len(s))   #O/P is 6 which is the length of string


#string slicing
    #two kinds  ->positive index
    #           ->negative index
s="qwerty"
print(s[0],s[1],s[2],s[3],s[4],s[5])    #O/P is q w e r t y    ->positive indexing
print(s[-1],s[-2],s[-3],s[-4],s[-5],s[-6])  #O/P is y t r e w q   ->negative indexing


#substring using slicing
#syntax: [start:stop:step] if step is is not given then it is 1 by default
a="Pomegranate"
s1=a[0:4]   #stop value should be index+1
print(s1)   #O/P is Pome
print(a[::-1])  #O/P is etanargemoP; when step is negative it goes in reverse


s="ABC d3f ghi"
print(s[3:len(s)-1])   # d3f gh
print(s[4:0:-1])        #d CB   ->A not inculded since it takes before the stop value
print(s[6:3])   #prints nothing


    
#print statement is output statement. It prints the output
a=3
b="idiots"
print(a,b)  #o/p is 3 idiots
print(str(a)+b) #o/p is 3idiots concatenation by type conversion



#Input:
    #It takes the input from the user
text=input("type any:")    #asks for input and if give "to" or if a number is given still it will take it as string.
print(5*text)       #o/p will be tototototo
 

#Task
s=input("Enter a verb:")
print("i can",s,"better than you")
print(5*(s+" "))  

#f stings   ->Formatted string value. 
           #->contents inside curly braces gets evaluated and converted to string
print(f'{3000*1/3} is {1/3*100}% of 3000')  



    
#Comparison operators   >,>=,<,<=,==,!=    
#logic operators  and, or, not
#Task guessing num
secret=5
guess=int(input("Guess the number:"))   
print(secret==guess)


#Branching:
    #making conditions with if,else,elif
#elif -> else+if which is basically nested else if

ptime=2
stime=10
if(ptime+stime)>24:
    print("impossible")
elif (ptime+stime)>=24:
    print("full schedule")
else:
    left=abs(24-ptime-stime)
    print(left,"hr left")
print("end of the day")
#12 hr left end of the day is the output
 

#Task
secret=55
guess=int(input("Enter a guess:"))
if (secret==guess):
    print("It is same as the secret number")
elif (secret>guess):
    print("Guess is too low")
else:
    print("Guess is too high")
    
    

    
    
    
    
    