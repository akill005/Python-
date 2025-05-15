#loops over strings, guess and check, and binary

#break statement
    #break keyword breaks the loop if the specified condition is met
#for eg,
mysum=0
for i in range (5,11,2):
    mysum+=i
    if mysum==5:
        break
print(mysum)
#o/p is 5 because mysum is 5 in 1st step itself so it gets terminated


#Task for finding even number counts in the ranges
#range(5)
count=0
for i in range (1,5):
    if(i%2)==0:
        count+=1
print(count)

#range(10)
count=0
for i in range (10):
    if(i%2)==0:
        count+=1
print(count)

#range(2,9,3)
count=0
for i in range (2,9,3):
    if(i%2)==0:
        count+=1
print(count)



#strings and loops
s="I love python"
for char in s:
    if char in 'ot':   #if char =='o' or char=='t'
        print("There's a o or t")
    
#cheer program
vows="aefhilmnorsxAEFHILMNORSX"
word=input("Give me a word:")
times=int(input("Enthustiatic level(1-10):"))
for i in word:
    if i in vows:
        print("Give me an:",i)
    else:
        print("Give me a:",i)
for i in range(times):
    print(word,"!!!")



#Task
#no. of unique letters in string
s="qsxcqqwadqqqw"
s1=""
count=0
for c in s:
    if c not in s1:
        s1+=c
        count+=1
print(count,s1)
#print(len(s1))    instead of using count we can go with length of unique letters string


#checks if its a square root 
guess=1
num=int(input("Enter a positive integer:"))
while (guess**2<num):
    guess+=1
if(guess**2==num):
    print(f'The square root of {num} is {guess}')
else:
    print('This is not a perfect square')


        
 #handling negative integers
guess=1
neg=False
num=int(input("Enter a positive integer:"))
if(num<0):
    neg=True
while (guess**2<num):
    guess+=1
if(guess**2==num):
   print(f'The square root of {num} is {guess}')
else:
    print('This is not a perfect square')
    if (neg):
        print("did you mean...",abs(num))

    

#secret num
secret=5
found=False
for i in range (1,11):
    if i==secret:
        found=True
if found:
    print("Found")
else:
    print("not found")
 
    
 
#cube root handling negative side also
cube=int(input("Enter a num:"))
for guess in range (abs(cube)+1):
    if(guess**3>=abs(cube)):
        break
if(guess**3!=abs(cube)):
    print("Not a cube root")
else:
    if(cube<0):
        guess=-guess
    print("Cube root of ",cube,'is',guess)

    
 
#computaional problems
#total tickets 10, A sold x, B sold x-2,c sold 2x. How much A sold?
for a in range(11):
    b=max(a-2,0)
    c=a*2
    if a+b+c==10:
        print("a sold",a)
        print("b sold",b)
        print("c sold",c)


#the ans is not same        
x=0
for i in range (10):
    x+=0.1
print(x,'==',10*0.1)



        
    
 #decimal to binary conversion
n=int(input("Enter any positive number:"))
res=''
while(n>0):
    res=str(n%2)+res
    n//=2
print(res)
 



   
#binary to decimal conversion
n=int(input("Enter any bin num:"))
res=0
num=str(n)
for i in range (len(num)):
    last=n%10
    res=(last*(2**i))+res
    n//=10
print(res)
    
 
    
 
    
  