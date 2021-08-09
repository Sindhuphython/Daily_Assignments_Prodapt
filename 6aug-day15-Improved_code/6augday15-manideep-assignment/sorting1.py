import timeit,logging
try:
    a=[12,123,453,44,345]
    def function1():
        a.sort()
    def function2():
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if a[j] > a[j+1]:
                    a[j+1], a[j] = a[j], a[j+1]
    print(timeit.timeit(function1,number=10000))


    print(timeit.timeit(function2,number=10000))                        

except:
    logging.error("opps!somethig went wrong")
finally:
    print("thanks")