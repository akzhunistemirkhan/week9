n = int(input())
if n%4==0 and n%100!=0:
    if n%400==0:
        print("YES")
elif n%4!=0:
    print("NO")