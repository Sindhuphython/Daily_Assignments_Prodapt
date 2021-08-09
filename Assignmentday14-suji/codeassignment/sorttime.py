import timeit
try:
    a=[236,104,856,798,12,465,672,6254,426]
    def f1():
        a.sort()
    #print(a)

#f1() 
    def f2():
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if a[j] > a[j+1]:
                    a[j+1], a[j] = a[j], a[j+1]
    #print(a)
               
            
#f2()
    print(timeit.timeit(f1,number=10000))                
    print(timeit.timeit(f2,number=10000))                        

except:
    logging.error("something went wrong")