a=[4,6,1,8,3,2,0,3]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            tem = a[j]
            a[j] = a[i]
            a[i] = tem
        else:
            pass
print(a)