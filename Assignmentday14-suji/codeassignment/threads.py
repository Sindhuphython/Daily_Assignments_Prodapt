import threading,logging
try:
    def prime():
        a = int(input("Enter lower range: "))  
        b = int(input("Enter upper range: "))  
  
        for num in range(a,b + 1):
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        break  
                    else:
                        print(num,end=" ") 
                        break     


    def palindrome():
        x=int(input("Enter lower number:"))
        y=int(input("Enter higher number:"))
        for num in range(x, y + 1):
            temp = num
            reverse = 0
            while(temp > 0):
                Reminder = temp % 10
                reverse = (reverse * 10) + Reminder
                temp = temp //10

            if(num == reverse):
                print("%d " %num, end = '  ')

    p=threading.Thread(target=prime)    
    q=threading.Thread(target=palindrome)
    p.start()
    q.start()
    p.join()
    q.join()
    print("*******")     

except:
    logging.error("something is wrong")           
              


