#Exceptions and assertions

def sum_dig(s):
    tot=0
    for char in s:
        try:
            val=int(char)
            tot+=val
        except:
            print("can't convert",char)
    return tot
s=input('Enter digits:')
print(sum_dig(s))



#specific exception
def div():
    a=int(input('enter a num'))
    b=int(input('enter another num'))
    try:
        print('a/b is',a/b)
        print('a+b',a+b)
    except ValueError:
        print("couldn,t convert to a number")
    except ZeroDivisionError:
        print('a/b is infinity')
        print('a+b is ',a+b)
div()



def sum_dig(s):
    tot=0
    for char in s:
        try:
            val=int(char)
            tot+=val
        except:
            raise ValueError("String contained character")
    return tot
s=input('Enter digits:')
print(sum_dig(s))




#assertion

def sum_dig_assert(s):
    assert len(s)!=0, " s is empty "
    tot=0
    for char in s:
        try:
            val=int(char)
            tot+=val
        except:
            raise ValueError("String contained character")
    return tot
s=input('Enter digits:')
print(sum_dig_assert(s))






def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("No grades given")
        return 0.0
def get_stats(li):
    new=[]
    for stud in li:
        new.append([stud[0],stud[1],avg(stud[1])])
    return new
li=[[['peter'],[80.0,90.0,85.0]],[['parker'],[65.0,79.0,90.0]]]
l1=[[['peter'],[80.0,90.0,85.0]],[['parker'],[]]]
print(get_stats(l1))
print(get_stats(li))












