#write a program to print strong numbers in a range using function?
def strong(n,m):
    for i in range(n,m+1):
        x,sum=i,0
        while i > 0:
            digit=i%10
            fact=1
            for j in range(1,digit+1):   # range=(100,100000)= 145,40585 are strong numbers
                fact*=j
            sum+=fact
            i//=10
        if sum==x:
            print(x)          
n,m=int(input()),int(input())
strong(n,m)
        



















