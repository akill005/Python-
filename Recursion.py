#Recursion
def mul(a,b):
    if b==1:
        return a
    else:
        return a+ mul(a,b-1)
print(mul(4,5))



def pow_rec(n,p):
    if p==0:
        return 1
    else:
        return n*pow_rec(n, p-1)
print(pow_rec(2,10))


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5)) 


     
