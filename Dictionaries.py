# Dictionaries
#key:value      keys->unique
#mutable
grades={'ana':'a','bell':'a'}
print(grades['bell'])
#access value by key but not vice versa


def find_grade(li,val):
    new=[]
    for i in val:
        grade=li[i]
        new.append(grade)
    return new
dic={'Matt':'A','Ross':'B','Mon':'A+','Rach':'B+'}
print(find_grade(dic,['Mon','Ross']))

#add,change , del any entries
dic['ATG']='O'
dic['Matt']='A+'
del(dic["ATG"])
for i in dic:
    print(i,dic[i])


#in keyword checks only keys
#Task
def find_key(ld,k):
    for char in ld:
        if k in char:
            return True
    return False
d1={1:2,3:4,5:6}
d2={2:4,4:6,6:8}
d3={1:1,3:9,5:25}
print(find_key([d1,d2,d3], 2))
print(find_key([d1,d2,d3], 25))


#keys, values and items #acts like tuple
print(list(d1.keys()))
print(list(d2.values()))
print(list(d3.items()))


def count(d):
    count=0
    for k,v in d.items():
        if k==v:
            count+=1
    return count
d1={1:2,2:3,4:5}
d2={1:2,'a':'a',5:5}
print(count(d1))
print(count(d2))


grades={'Ana':{'eng':[4,8],'cs':[6,8,9]},
        'Bell':{'cs':[10,3,7],'eng':[6,10]}}
#print(grades['Ana']['eng'][2])
def avg(data,what):
    all_data=[]
    for stud in data.keys():
        all_data=all_data+data[stud][what]
        print(all_data)
    return sum(all_data)/len(all_data)
print(avg(grades,'eng'))    


#frequency dictionary
song='baby baby baby oh oh oh i love punch'
def word(s):
    s_low=s.lower()
    s_list=s_low.split(' ')
    word_dict={}
    for i in s_list:
        if i in word_dict:
            word_dict[i]+=1
        else:
            word_dict[i]=1
    return  word_dict
a=word(song)
# print(a)


a={'baby': 3, 'oh': 3, 'i': 1, 'love': 1, 'punch': 1}
def high(word_dict):
    w=[]
    hi=max(word_dict.values())
    for k,v in word_dict.items():
        if v==hi:
            w.append(k)
    return (w,hi)
print(high(a))



def often(dic,freq):
    freq_list=[]
    words_with_freq=high(dic)
    while words_with_freq[1]>freq:
        freq_list.append(words_with_freq)
        words_with_freq=high(dic)
        for i in words_with_freq[0]:
            del(dic[i])
    return freq_list
print(often(a,1))
    


