#Find prime numbers between 2 and 500
import logging
import time,multiprocessing

logging.basicConfig(filename='Execution.log', level=logging.INFO)

#Finding Prime Numbers
l = 2
u = 500

def prime(l,u):
    for n in range(l, u + 1):
        if n > 1:                       # all prime numbers are greater than 1
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)

#Finding Polindrome Numbers
min =10
max = 500

def polindrome(min,max):
    for num in range(min, max + 1):
        temp = num
        reverse = 0
        
        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10
        if(num == reverse):
            print("%d " %num, end = '  ')


if (__name__)=="__main__":

    #print(timeit.timeit(prime (stmt= )))
    #print(timeit.timeit(prime,   ))
    # print(timeit.timeit(polindrome))
    
    p1=multiprocessing.Process(target=prime, args=(l,u,))
    p2=multiprocessing.Process(target=polindrome, args=(min,max,))
    p1.start()
    p2.start()
    p1.join()
    print("Prime numbers are printing")
    
    p2.join()
    print("Polindrome numbers are printing")
   
   
    try:
        print("....")
        
        
        logging.info("Prime and Polindrome numbers are printed successfully by multiprocessing")
        #logging.info(timeit.timeit(prime))
    except:
        logging.error("An unkown error happened")



    
        

           