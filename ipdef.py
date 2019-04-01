# Python Program to Get IP Address 
import socket    
hostname = socket.gethostname()    
ip1 = socket.gethostbyname(hostname)    
print("IP>>"+ip1)
#now we have to count the network id and host id
#for this we have to count 1 and o in the ip1(after binary conversion)
#so
ip2=str(ip1)
q,w=str(ip2.count('1')),str(ip2.count('0'))
##now i am taking cidr value from user
cidr=int(input("enter the cidr value>>"))
ni=cidr
if cidr<=32:
    hi=32-ni
    print("your network bits>>"+str(ni))
    print("host bits >>"+str(hi))
    a=['1'*(ni-1),'0'*(hi+1)]
    a1=''.join(a)
    a3=[]
    for y in range (1):
        a4=a1[0:7]
        a5=a1[7:15]
        a6=a1[15:23]
        a7=a1[23:31]
        a3.append(a4)
        a3.append(a5)
        a3.append(a6)
        a3.append(a7)
        #print("binary conversion>>" + ".".join(a3))
        l=list(a3[3])
        #print(l)
        x=0
        c=7
        z=[]
        #print(a7)
        str(a7)
        h=a7.count("1")
        k=a7.count("0")
        
        print("number of network>>" + str(2**h))
        print("number of ip address on each network>>" + str(2**k))
        print("number of hosts in each network>>" + str(2**k -2))
        l2=["255","255","255"]
        
        if h==1:
            l2.append("128")
            l3=".".join(l2)
            print("subnet>>" + l3)
        elif h==2:
            l2.append(str(128+64))
            l3=".".join(l2)
            print("subnet>>" + l3)
        elif h==3:
            l2.append(str(128+64+32))
            l3=".".join(l2)
            print("subnet>>" + l3)
        elif h==4:
            l2.append(str(128+64+32+16))
            l3=".".join(l2)
            print("subnet>>" + l3)
        elif h==5:
            l2.append(str(128+64+32+16+8))
            l3=".".join(l2)
            print("subnet>>" + l3)
        else:
            print("I can't calculate anymore")
else:
    print("wrong cidr value")