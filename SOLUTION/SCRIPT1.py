# writer a program to print number ia a prime or not prime
n=int(input('enter any number:'))
count=0
i=1
while i<=n:
    if(n%i==0):
        count+=1
        i+=1
        if count==2:
            print("prime number")
        else:
            print("not prime number")
