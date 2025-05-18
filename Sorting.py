# Sorting
import random
import time

#bogo sort  unbounded
def isort(l):
    i=0
    j=len(l)
    while i+1<j:
        if l[i]>l[i+1]:
            return False
        i+=1
    return True
def bogo(l):
    count=0
    while not isort(l):
        random.shuffle(l)
        count+=1
    return count
    
l=[6,3,6,1,9,0,4,6,5]
print('l:       ',l)
t0=time.time()
count=bogo(l)
print('sorted',l)
print(count,'shuffles and sorting took',time.time()-t0)
    

#bubble sort   O(n^2)

def bub(l):
    swap=True
    while swap:
        swap=False
        for j in range (1,len(l)):
            if l[j-1]>l[j]:
                swap=True
                l[j],l[j-1]=l[j-1],l[j]
      
            print(l)
l=[8,5,6,3,8,4,1,3,0]
print('l:            ',l)
bub(l)
print('sorted',l)


#selection sort   O(n^2)
def sel(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[j]<l[i]:
                l[i],l[j]=l[j],l[i]
                print(l)
l=[8,5,6,3,8,4,1,3,0]
print('l:            ',l)
sel(l)
print('sorted',l)


#merge    O(nlogn)
def merge(left,ri8):
    res=[]
    i,j=0,0
    while i<len(left) and j<len(ri8):
        if left[i]<ri8[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(ri8[j])
            j+=1
    while (i<len(left)):
        res.append(left[i])
        i+=1
    while (j<len(ri8)):
        res.append(ri8[j])
        j+=1
    return res
 
def mergee(l):
    if len(l)<2:
        return l[:]
    else:
        middle=len(l)//2
        left=mergee(l[:middle])
        ri8=mergee(l[middle:])
        return merge(left,ri8)
l=[8,5,6,3,8,4,1,3,0]
print(mergee(l))




   