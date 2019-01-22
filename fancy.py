t=int(input())
list1=[]
for _ in range(t):
    s=input().lower()
    s=s.split()
    if 'not' in s:
        list1.append("Real Fancy")
    else:
        list1.append("regularly fancy")
for i in list1:
    print(i)
