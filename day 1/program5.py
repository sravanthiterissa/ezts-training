#a,b=map(int,input().split(" "))  - we can write input values side by side
'''a,b=map(int,input().split(" "))
print(a,b)'''

'''a,b=map(float,input().split(" "))     #b=balance amount,a=withdrawl amount
if b>a:
    if a%5==0:
        print(b-a)
    else:
        print(b)
else:
    print(b)'''

a,b=map(float,input().split(" "))
if b>a and a%5==0:
        print(b-a)
else:
        print(b)


