
#Lecture 3 - Iteration

#while loop:
#    syntax -> while(expn):
                    # code block
#Example
n=int(input("Enter non negative int:"))
while(n>0):
    print(n)
    n=n-1
#It checks the condn and runs upon it to execute the block of codes inside while. Once condn fails it terminates the loop




#Factorial program using while
x=5
i=1
fact=1
while(i<=x):
    fact*=i
    i+=1
print(f'{x} factorial is {fact}')



#for loop
#since while is verbose for loop is created. It gives less code lines when compared to while
#syntax: for <variable> in range <some_num>:  ....codes....
#range(start,stop,step)  just like substring

#Examples
 #running sums
mysum=0
for i in range (10):
    mysum+=i
print(mysum) 
#o/p is 45   



#factorial using for loop
x=5
fact=1
for i in range (1,5+1):
    fact*=i
print(fact)
    



