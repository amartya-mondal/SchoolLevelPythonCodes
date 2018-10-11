# HCF OF TWO NUMBER.....

def fact(x,y):
    if x>y:
        low=y
    else:
        low=x
    while(True):
        if ((x%low==0) and (y%low==0)):
            hcf=low
            break
        else:
            low=low-1
    return hcf

def main():
    x=int(input("Enter the 1st number "))
    y=int(input("Enter the 2nd number"))
    hcf=fact(x,y)
    print("HCF of {} and {} is {}".format(x,y,hcf))

main()
