#telephonbooth
'''n=int(input())
d={}
for i in range(n):
    key,value=map(str,input().split())
    d[key]=value
for i in range(n):
        s=input()
        if s in d:
            print(s,d[s])
        else:
             print("not found")'''
#to get no of search items

n=int(input())
d={}
for i in range(n):
    key,value=map(str,input().split())
    d[key]=value
m=int(input("no of search items: "))    
for i in range(m):
        s=input()
        if s in d:
            print(s,d[s])
        else:
             print("not found")


             
