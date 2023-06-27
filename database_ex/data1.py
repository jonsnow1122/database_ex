import numpy as np
import random

cdata=open('C:/Users/lenovo/Desktop/classdata.txt')

#data1=open('C:/Users/lenovo/Desktop/数据库实验/data1.txt','w')
#data2=open('C:/Users/lenovo/Desktop/数据库实验/data2.txt','w')
data3=open('C:/Users/lenovo/Desktop/数据库实验/data3.txt','w')
#stu=('C:/Users/lenovo/Desktop/数据库实验/1.txt','r')
sid_list=[]
cid_list=[]
sc_set=set()

def random_grade():
    if random.choice(range(100))<20: #20%概率不及格
        return str(round(random.uniform(0,59),1))
    else:
        return str(round(random.uniform(60,100),1))

c=int(input()) #20000
#data1.write("s#\tsname\tsex\tbdate\theight\tdorm\n")
#data2.write("c#\tcname\tperiod\tcredit\tteacher\n")
data3.write("s#\tc#\tgrade\n")
sno_numpy = np.loadtxt('C:/Users/lenovo/Desktop/数据库实验/1.txt', skiprows=2, dtype=str, usecols=(0), encoding='UTF-8')
cno_numpy = np.loadtxt('C:/Users/lenovo/Desktop/数据库实验/data2.txt', skiprows=1, dtype=str, usecols=(0), encoding='UTF-8')
for i in range(0,1000):
    sid_list.append(sno_numpy[i])
for i in range(0,100):
    cid_list.append(cno_numpy[i])

while c>0:#创建SC742数据
    sid=random.choice(sid_list)
    cid=random.choice(cid_list)
    if(sid,cid) in sc_set:
        continue
    else:
        sc_set.add((sid,cid))
    data3.write(sid)
    data3.write("\t")
    data3.write(cid)
    data3.write("\t")
    data3.write(random_grade())
    data3.write("\n")
    c=c-1
data3.close()