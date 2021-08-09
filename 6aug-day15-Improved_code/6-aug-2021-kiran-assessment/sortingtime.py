import timeit
data=[12,15,54,63,25,18,41,78,23]
def sorting():
    a=sorted(data)
    pass

def bubble_sort():
    length=len(data)
    i=data[0]
    j=data[0]
    for i in range(length-2):
        for j in range (length-2-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    pass
def insertion_sort():
    length=len(data)
    for i in range(1,length):
        item=data[i]
        j=i-1
        while(j>=0 and data[j]>item):
            data[j+1]=data[j]
            j=j-1
        data[j+1]=item
print(timeit.timeit(sorting,number=100000))
print(timeit.timeit(bubble_sort,number=100000))
print(timeit.timeit(insertion_sort,number=100000))