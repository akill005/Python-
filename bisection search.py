# bisection search algorithm
# guessing the value by half and make a decision and then continue untill the req ans
# fast when compared to previous session
x=543321
gcount=0
epsilon=0.01
low=0
high=x
guess=(low+high)/2.0
while abs(guess**2 - x)>=epsilon:
    if guess**2<x:
        low=guess
    else:
        high=guess
    guess=(low+high)/2.0
    gcount+=1
print('num of guess',gcount)
print('closed guess is',guess)



#for finding values in ranges 0 to 1
x=int(input("Enter any num to find its sq root:"))
gcount=0
epsilon=0.01
if x>=1:
    low=1.0
    high=x
else:
    low=x
    high=1.0
guess=(low+high)/2.0
while abs(guess**2 - x)>=epsilon:
    if guess**2<x:
        low=guess
    else:
        high=guess
    guess=(low+high)/2.0
    gcount+=1
print('num of guess',gcount)
print('closed guess is',guess)




#cube roots
x=27
high=x
low=0
epsilon=0.01
gcount=0
guess=(low+high)/2.0
while(abs(guess**3 - x)>=epsilon):
    if guess**3<x:
        low=guess
    else:
        high=guess
    gcount+=1
    guess=(low+high)/2.0
print('gcount',gcount)
print('closed guess is',guess)





#newton raphson #root finder 
#formula is for x^2-k   -> g-(g*g - k)/2g 
ep=0.01
k=54321
g=k/2.0 #guess
gcount=0
while (abs(g**2 - k)>=ep):
    gcount+=1
    g-=((g*g)-k)/(2*g)
print(gcount)
print(g)



