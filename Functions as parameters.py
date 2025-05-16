#fn as obj


# def is_triangular(n):
#     total = 0
#     for i in range(n):
#         total += i
#         if total == n:
#             return True
#     return False
# print('7 tri?',is_triangular(7))
# print('15 tri?',is_triangular(15))



#with bisection search
# def root(n):
#     epsilon=0.01
#     low=0
#     high=n
#     guess=(low+high)/2.0
#     while abs((guess**2 - n)) >= epsilon:
#         if(guess**2)>n:
#             high=guess
#         else:
#             low=guess
#         guess=(low+high)/2
#     return guess
# print(root(150))
# print(root(4))



#nums closed to sq root within epsilon range
# def count_root(n,ep):
#     count=0
#     for i in range (n**3):
#         sqrt=root(i)
#         if abs(n-sqrt)<ep:
#             count+=1
#             print(i,sqrt)
#     return count
# print(count_root(10,1))
# print(count_root(10,0.1))
    
    

#local and global variables
# def g(y):
#     print(x)
#     print(x+1)    #checks if there's a x if found take it or produce erro'
# x=5
# g(5)
    
#fns as parameters
# def calc(op,x,y):
#     return op(x,y)
# def add(a,b):
#     return a+b
# def div(a,b):
#     if b!=0:
#         return a/b
#     print("Denominator is 0")
# print(calc(add,2,3))
# print(calc(div,2,0))   
    
 
    
 
    #task
def apply(crit,n):
    '''crit is fn that takes a num and return bool
    n is int
    returns how many ints from 0 to n (inclusive)'''
     
    count=0
    for i in range (n+1):
        if crit(i):
            count+=1
    return count
def is_even(n):
    return n%2==0
print(apply(is_even,10))
    
    
    
    
    
    
    
    