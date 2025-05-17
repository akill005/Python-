#Recursion on non numericx
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(8))







#using dic
def fibd(n,d):
    if n in d:
        return d[n];
    else:
        ans=fibd(n-1,d)+fibd(n-2,d)
        d[n]=ans
        return ans
d={1:1,2:1} 
print(fibd(8,d))





#recursion in list
#sum of list elements
def sum_li(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0]+sum_li(l[1:])
li=[1,2,3,4,5]
print(sum_li(li))





l1=["asd","qweer","a<3p"]
def len_li(l):
    if len(l)==1:
        return len(l[0])
    else:
        return len(l[0])+len_li(l[1:])
print(len_li(l1))




def inlist(li,x):
    if len(li)==0:
        return False
    elif li[0]==x:
        return True
    else:
        return inlist(li[1:], x)
li=[1,2,3,4,5]
print(inlist(li,6))



#flatten list
def flatten(li):
    if len(li)==1:
        return li[0]
    else:
        return li[0] + flatten(li[1:])
li=[[1,2],[3,4],[4,5]]
print(flatten(li))
 


#reverse a list
def rev(li):
    if len(li)==1:
        return li
    else:
        return rev(li[1:])+[li[0]]
print(rev([2,3,7,15,6]))




def deeprev(l):
      if len(l)==1:
          if type(l[0])!=list:
              return l
          else:
              return [deeprev(l[0])]
      else:
        if type(l[0])!=list:
            return deeprev(l[1:])+[l[0]]
        else:
            return deeprev(l[1:])+[deeprev(l[0])]
l=[[1,2],3,4,[[5,6],[7,8]]]
print(deeprev(l))




#better code
def deep(l):
    if l==[]:
        return []
    elif type(l[0])!=list:
        return deep(l[1:])+[l[0]]
    else:
        return deep(l[1:])+[deep(l[0])]
l=[[1,2],3,4,[[5,6],[7,8]]]
print(deep(l))






