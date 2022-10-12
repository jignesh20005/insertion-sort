#insertion sort ascending order
a=[80,20, 50, 60, 70, 40, 90, 100]
def insertionsort(a):
    b=1
    while b<len(a):
        i=b
        while i>0:
            if a[i]<=a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]

            else:
                break
            i=i-1
        b=b+1
    print(a)
insertionsort(a)
