#write script to enter any number and check it is armstrong or not
n=int(input("enter any armstrong:"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=sum+(r**3)
    n=n//10
    if temp==sum:
        print("armstrong number")
    else:
        print("not a armstrong number")
    
