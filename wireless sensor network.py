

import matplotlib.pyplot as plt
import numpy as np
N=10
A=50
count=0
countred=0
a=0
m=[]

nodes=np.round(1+(A-1)*np.random.random((N,2)))
plt.plot(nodes[:,0],nodes[:,1],'ko')

for i in range(N):
    plt.text(nodes[i,0],nodes[i,1],i)
plt.text(28,24,'GRAPH ANALYSIS')
plt.xlabel('x axis ')
plt.ylabel('y,axis')
print("nodes",nodes)
energy=np.full((10,1),1000)
print(energy)
new=[]
totalEG=[]
d=[]
rednode=[]

while(1):
    d=[]
    node=np.random.randint(10)
    print("node==",node)	
    c=nodes[node]
    for i in  range(N):
        plt.pause(0.2)
        distance=np.sqrt(np.square(nodes[i][0]-c[0])+np.square(nodes[i][1]-c[1]))
        if (distance>0 and distance<=15):
            print("neighbour=",nodes[i])
            d.append(i)

    print("index of neighbours=",d)
    ER=np.random.randint(100,200)
    ET=np.random.randint(100,200)
    energy[d]=(energy[d]-ER)
    energy[node]=(energy[node]-ET)
    energy[np.where(energy<0)]=0
    totalEG.append(np.sum(energy))
    for i in range(N):
        print("energy disipitate",energy[i])
        if(energy[i]>800 and energy[i]<1000):
            plt.plot(nodes[i][0],nodes[i][1],'bo')
        elif(energy[i]>500 and energy[i]<800):
            plt.plot(nodes[i][0],nodes[i][1],'yo')
        elif(energy[i]>100 and energy[i]<500):
            plt.plot(nodes[i][0],nodes[i][1],'ro')
            plt.pause(0.2)
            countred=countred+1
            m.append(i)

    
    d=m[::-1]
    print("countred",countred)
    count=count+1
    print("iterations",count)
    if (countred==1):
        a=count

    
    flag=0
    for i in range(N):
        if(energy[i]>500):
            flag=1
            break
    plt.ioff()   
    if(flag==0):
        break
    
for i in range(countred):
    for i in range(len(d)):
        if(d.count(i)>1):
            d.remove(i)
rednode=d[::-1]            
print("sequence of red nodes",rednode)
print("first red node is ",rednode[0],"in",a,"itterations")
print("last node red is",rednode[-1],"in",count,"itteration")
print("total iterations",count)
print("total energy",totalEG)
       
    
def energy_graph():
    plt.figure(2)
    g=plt.plot(totalEG[:],'g')
    plt.text(28,24,"Energy Disipation Graph")

    plt.show(g)
energy_graph()    

def nodes_graph():
    plt.figure(3)
    f=plt.plot(rednode[:],'ro')
    f=plt.plot(rednode[:],'r')
    for i in range(len(rednode)):
        plt.text(i,rednode[i],rednode[i])
    plt.text(28,24,"Nodes Disipation Graph")
    plt.show(f)
    
nodes_graph()    

