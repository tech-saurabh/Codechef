import string
alphabet=string.ascii_lowercase
t=int(input())
d=[]
while(1<=t<=100):
    for _ in range(t):
        a=int(input())
        for _ in range(a):
            f=alphabet.index(input())
            d.append(f)
    for i in d:
        print(i)
