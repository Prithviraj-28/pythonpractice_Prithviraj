import time
import threading
def sumeven(no): #will perform 2+4+6+8 = 20
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i 
    print("summation of even :",sum)

def sumodd(no):  #will perform 1+3+5+7+9 = 25
    sum = 0
    for i in range(1,no+1,2):
        sum = sum + i 
    print("summation of odd :",sum)

def main():
    start_time= time.perf_counter()

    t1= threading.Thread(target=sumeven,args=(100000000,))  #writing integer 100000000 as (100000000,) so it becomes a tuple 
    t2=threading.Thread(target=sumodd,args=(100000000,))    #and can be passed as an argument to the function sumeven and sum odd,
    t1.start() #starting thread t1                          # otherwise it will be treated as an integer and will give error
    t2.start()  #starting thread t2
    t1.join()  # joins the time of main thread and the time of thread t1 and t2, so that the main thread will wait for the
    t2.join()  #completion of t1 and t2
    
    end_time= time.perf_counter() #issue resolved

    print(f"Time required is : {end_time-start_time:.5f}")

if __name__ == "__main__":
    main()