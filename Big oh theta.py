# # Timing details
import time
# def convert(m):
#     return m*1.609
# def compound(inv,interest,n):
#     tot=0
#     for i in range(n):
#         tot=tot*interest+inv
#     return tot
# t0=time.perf_counter()
# convert(100000)
# dt=time.perf_counter()-t0
# print('t=',dt,'s,')
# l=[1]
# for i in range(7):
#     l.append(l[-1]*10)
# for n in l:
#     t0=time.perf_counter()
#     km=convert(n)
#     dt=time.perf_counter()-t0
#     print(f"convert({n}) took {dt:.2e} sec ({1/dt:,.2f}/sec) ")
# for n in l:
#     t0=time.perf_counter()
#     mon=compound(10.0,1.05,n)
#     dt=time.perf_counter()-t0
#     print(f"compound({n}) took {dt:.2e} sec ({1/dt:,.2f}/sec) ")
   
    
# def sumof(l):
#     tot=0.0
#     for i in l:
#         tot+=i
#     return tot
# l=[1]
# for i in range(7):
#     l.append(l[-1]*10)
# for n in l:
#     li=list(range(n))
#     t=time.perf_counter()
#     s=sumof(li)
#     dt=time.perf_counter()-t
#     print(f"sumof({n}) took {dt}sec ({1/dt})sec")


    
#counting    
    
# def isin(l,x):
#     global c
#     c=1
#     for e in l:
#         c+=2
#         if e==x:
#             return True
#     return False
    
# l=[1]
# for i in range(5):
#     l.append(l[-1]*10)

# count=[]
# for i in l:
#     ct=0
#     L=range(i)
#     for x in [L[0],L[len(L)//2],L[-1]]:
#         my=isin(L,x)
#     print(ct,'sec')
#     count.append(ct)
    
    
    
    