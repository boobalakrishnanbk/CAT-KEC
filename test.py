n = int(input())
a = [int(input()) for i in range(n)]
count = 0
for door in range(n):
    if a[door]==0:
        pass
    else:
        count += 1
        for j in range(door,n):
            if a[j]==1:
                a[j]=0
            else: or a[j] = 1
print(count)