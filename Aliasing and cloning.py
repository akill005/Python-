#Aliasing and cloning

def remove_all(L,e):
    l_copy=L[:]
    L.clear()
    for i in l_copy:
        if i != e:
            L.append(i)
li=[1,2,2,3,3,2,]
e=2
remove_all(li, e)
print(li)


#remove()    ->removes 1st occurence only
#l.remove(2)
#del(l[index])  ->del val in specific index
#pop() -> del the last element


def rem_dup(l1,l2):
    l1_copy=l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)
    return l1
l1=[1,2,3,2,45,4,6,]
l2=[45,6]
rem_dup(l1, l2)
print(l1)


import copy
old=[[1,2],[3,4]]
new=copy.copy(old)
old.append([2,9])
old[1][1]=5
print(new)
print(old)


