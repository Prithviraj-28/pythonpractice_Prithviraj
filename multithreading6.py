import time
import threading
def sumeven(no): #will perform 2+4+6+8 = 20
    sum = 0
    for i in range(2,no,2):
        sum = sum + i 
    print("summation of even :",sum)

def sumodd(no):  #will perform 1+3+5+7+9 = 25
    sum = 0
    for i in range(1,no,2):
        sum = sum + i 
    print("summation of odd :",sum)

def main():
    start_time= time.perf_counter()

    t1= threading.Thread(target=sumeven,args=(100000000,))
    t2=threading.Thread(target=sumodd,args=(100000000,))
    t1.start()
    t2.start()
    
    end_time= time.perf_counter() #should wait until both threads are over  so time is displayed before threads are over 

    print(f"Time required is : {end_time-start_time:.5f}")

if __name__ == "__main__":
    main()