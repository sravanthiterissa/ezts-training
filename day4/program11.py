#to print a list of vowels,count of vowels, in a given each word of a sentence using functions?

def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i.lower() in "aeiou":
            vc+=1
            s1+=i
    print("Vowel count:",vc)
    print(list(set(s1)))        
l=input().split()
for i in l:
    counting(i)