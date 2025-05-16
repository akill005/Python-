#list comprehension, fn as objects,testing

print([i**2 for i in range(1,6)])


#default parameter
def bisection(num, ep=0.01):    #0.01 is default if user didn't care to give any

    low=0
    high=num
    guess=(low+high)/2
    while abs(guess**2 - num)>=ep:
        if abs(guess**2)>=num:
            high=guess
        else:
            low=guess
        guess=(low+high)/2
    return guess
guess=bisection(25,1)
print(f"closed guess is {guess}")




def m(a):
    def g(b):
        return a*b
    return g
print(m(2)(3))

#Testing approaches
# Black ox and glass box

# blackbox:
#     Explore through specification
#     only seeing doc string and test
    
# Glass box:
#     use the code for test
#     seeing branches,loops
    









