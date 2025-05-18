#plotting
#plt.plot(<x val>,<y val>)
import matplotlib.pyplot as plt
nval=[]
linear=[]
quad=[]
cubic=[]
exp=[]
for i in range(0,30):
    nval.append(i)
    linear.append(i)
    quad.append(i**2)
    cubic.append(i**3)
    exp.append(1.5**i)
    
plt.plot(nval,linear)
plt.figure('lin')
plt.scatter(nval,linear)
plt.figure("quad")
plt.plot(nval,quad)
plt.figure("cubic")
plt.plot(nval,cubic)
plt.figure("expo")
plt.plot(nval,exp)
plt.show()





months=range(1,13,1)
temps=[28,32,19,20,74,95,36,25,45,28,12,54]
temp=[12,34,43,6,46,67,90,89,8,6,4,56]
plt.subplot(2,1,1)
plt.xlim(1,12)
plt.ylim(1,100)
plt.plot(months,temps,'*b-',label="boston",linewidth=10)
plt.subplot(2,1,2)
plt.plot(months,temp,'or--',label="LA")
plt.title("TEMP")
plt.xlabel("Months")
plt.ylabel("temp")
plt.xlim(1,12)
plt.ylim(1,100)
plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12),('Jan','Feb','Mar','April','May','June','July','August','Sept','Oct','Nov','Dec'))
plt.grid()
plt.legend()
plt.show()



def getdata(fileName):
    inFile=open(fileName,'r')
    dates,pops=[],[]
    for l in inFile:
        line=''
        for c in l:
            if c in '0123456789':
                line+=c
        line=line.split(' ')
        dates.append(int(line[0]))
        pops.append(int(line[1]))
    return dates,pops

dates,pops=getdata('link for text file dataset')
plt.plot(dates,pops)
plt.title('pop vs native')
plt.xlabel('Year')
plt.ylabel('Pop')






















