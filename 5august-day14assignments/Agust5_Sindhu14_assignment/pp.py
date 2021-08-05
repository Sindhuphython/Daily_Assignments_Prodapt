import multiprocessing,time
def primeNumbers():
    for i in range(2,500):
        time.sleep(3)
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print("primenumbers:",i)
def palindrome():
    for i in range(10,500):
        time.sleep(3)
        temp=i
        rev=0
        while(temp>0):
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
            if(i==rev):
                print("palindrome:",i)

if(__name__=="__main__"):
p1=threading.Thread(target=primeNumbers)
p2=threading.Thread(target=palindrome)
p1.start()
p2.start()
p1.join()
p2.join()
print("..........")
