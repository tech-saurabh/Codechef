import string
alphabet=string.ascii_lowercase
a=int(input())
d=[]
while(a<100):
    for _ in range(a):
        f=alphabet.index(input())
        d.append(f)
    for i in d:
        print(i)
    
