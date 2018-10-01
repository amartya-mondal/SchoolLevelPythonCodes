#INSERTION SORT
#_________________________________________________________________________________
class abc(object):
    def __init__(self):
        self.l=[]
        self.n=int(input("Enter no of elements to be sorted: "))
        for i in range(self.n):
            self.l+=[int(input("Enter the element: "))]

    def work(self):
        print ("The unsorted array is: ",self.l)
        for i in range(1,self.n):
            j=i-1
            temp=self.l[i]
            while j>=0 and temp<self.l[j]:
                self.l[j+1]=self.l[j]
                j-=1
            self.l[j+1]=temp
        print ("The sorted array in ascending order is: ",self.l)

obj=abc()
obj.work()

        
