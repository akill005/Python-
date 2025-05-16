# Mutablility of lists

#l.append(1)  correct
#l1=l.append(1)   wrong
#sort()   ->l.sort()
#reverse()  ->l.reverse()
#sorted()   ->l1=sorted(l)  ->Gives the copy of original list and sorts it

l1=['re']
l2=['mi']
l3=['do']
l4=l1+l2
l3.append(l4)
l=l1.append(l3)

#task
def order_list(n):
    li=[]
    for i in range (n+1):
        li.append(i)
    return li
print(order_list(6))



#removing given element
def remo_ele(l,e):
    l1=[]
    for i in l:
        if i!=e:
            l1.append(i)
    return l1
            
li=[1,2,3,4,3,2,4,5,1,6]    
print(remo_ele(li,2))




#strings to lists    ->split()
s='i love data analytics'
l1=s.split(' ')
l2=s.split('a')
print(l1,l2)


#lists to strings   ->join()  works with only string not int or any data type
l=['a','b','c']
print(''.join(l))
print('_'.join(l))
print(''.join(['1','2','3']))



#task
def count(sen):
    li=sen.split(' ')
    return len(li)
print(count('I love python'))



#ordering sentence
def sort_word(sen):
    l=sen.split()
    l.sort()
    return l
s='loot at me now'
print(sort_word(s))


#sq nums
def sq(li):
    for i in range(len(li)):
        li[i]=li[i]**2
    return li
print(sq([1,2,3,4,5]))



#for combining 2 lists we can use extend
l1=[1,2,3]
l1.extend([4,5,6])
print(l1)













