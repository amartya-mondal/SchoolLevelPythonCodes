#Armstrong number for 3 digit numbers
from math import pow
def enter(n,l):
    i=0
    while i<n:
        val=int(input("Enter the number: "))
        if val in range(100,1000):
            l+=[val]
            i+=1
    return l
#=============================================================================
def armstrong(num):
    trm=num
    s=0
    while num>0:
        r=num%10
        num//=10
        s+=pow(r,3)
    if s==trm:
        return True
    else:
        return False
#=====================================================================================
def main():
    flag=1
    while flag==1:
        n=int(input("Enter no of numbers u want to enter: " ))
        l=[]
        ans=[]
        l=enter(n,l)
        for i in l:
            check=armstrong(i)
            if check==True:
                ans+=[i]
            
        c=len(ans)
        if c==0:
            print ("No armstrong number found")
        else:
            print ("The armstrong numbers are ")
            a=str()
            for i in ans:
                a+=str(i)+" "
            print (a)
        flag=int(input("Press 1 to continue else press anything: "))
#============================================================================================
main()
