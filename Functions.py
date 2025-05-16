#Decomposition, abstraction and functions
#def div_by(n,d):
    # """n and d are ints
    # returns true if d evenly divides n else false"""


# n=10 d=3
def div_by(n,d):
    if (n%d==0):
        return True
    else:
        return False
n=195
d=13
print("is evenly divible?",div_by(n, d))




#can be called anytime
def is_even(i):
    if i%2==0:
        return True
    else:
        return False
for i in range (11):
    if is_even(i):
        print(i,"is even")
    else:
        print(i,"is odd")


#add integers exclusive between a and b
def is_odd(n):
    if(n%2==1):
        return True
    else:
        return False
def sum_odd(a,b):
    res=0
    for i in range(a+1,b):
        if is_odd(i):
            res=res+i
            print(res)
    return res
a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
print('sum of odd integers between a and b is',sum_odd(a, b))


#palindrome
def is_pali(s):
    s1=''
    s1=s1+s[::-1]
    if s1==s:
        return True
    else:
        return False
s=input("Enter any num or string for palindrome check:")
print("It is",is_pali(s))



#keeping consonants only
def keep_con(s):
    s1=''
    for i in range (len(s)):
        if s[i] not in 'aeiou':
            s1+=s[i]
    return s1
s='aeioubcdghjklbbbbb'
print(keep_con(s))



#diff between index occurances
def diff(s,c):
    for i in range (len(s)):
        if s[i]==c:
            ind1=i
            break
    for i in range (ind1,len(s)):
        if s[i]==c:
            ind2=i
    return ind2-ind1
s='cning'
c='n'
print(diff(s,c))



