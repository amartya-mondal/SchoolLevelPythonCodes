#                                   BUBBLE SORT
#--------------------------------------------------------------------------------------------
class prac(object):
    def __init__(self):
        self.l=[]
        self.n=int(input("Enter for no of elements: "))

    def work(self):
        for i in range(self.n):
            self.l+=[int(input("Enter value: "))]
        print ("The Array so far made is: ")
        print (self.l)

        for k in range(self.n):
            for j in range(self.n -1-k):
                if self.l[j]>self.l[j+1]:
                    temp=self.l[j+1]
                    self.l[j+1]=self.l[j]
                    self.l[j]=temp

        print ("The values in ascending order is: ")
        a=str()
        for i in (self.l):
            a+=str(i)+" "
        print (a)

obj=prac()
obj.work()
