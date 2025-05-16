#Lambda,tuples,lists

#lambda -> 1 line fn  ->ananymous fn 
if ((lambda x:x%2==0)(8)):
    print("Even")
    
    
#Tuple - immutable
#a=(5)    int
#a=(2,)   tuple
#works just like string
tup=(1,3,'ferry',5)
print(type(tup))
print(tup[2])
print(tup[::-1])

#swapping 
x=1
y=8
(x,y)=(y,x)
print(x,y)


#returns more than 1 element in return fn
def quo(x,y):
    q=x//y
    r=x%y
    return (q,r)
print(quo(10,2))


#task
def char_count(s):
    s1=''
    s2=''
    for i in range(len(s)):
        if s[i] in 'aeiou':
            s2+=s[i]
        else:
            s1+=s[i]
    tup=(s2,s1)
    return tup,len(s2),len(s1)
print(char_count('apple'))
            
            
def mean(*arg):
    tot=0
    for a in arg:
        tot+=a;
    return tot/len(arg)
print(mean(1,2,3,4,5,6))




#Lists
#mutable
l=[] #empty list
#[1,2]+[2,4]  ->o/p is [1,2,2,4]

#can loop directlt
def list_sum(l):
    tot=0
    for i in l:
        tot+=i
    return tot
print(list_sum([1,2,3,4,5]))


#task
def sum_prod(l):
    (s,p)=(0,1)
    for i in l:
        s+=i
        p*=i
    return (s,p)
li=[1,2,3,4,5]
print(sum_prod(li))










