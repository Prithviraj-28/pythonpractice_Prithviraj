import time
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    
    return fact

def main ():
    value = int(input("Enter the number : "))

    start_time = time.perf_counter()

    ret = factorial(value)

    end_time = time.perf_counter()

    print(f"Factorial of {value} is : ",ret)   
    print(f"Time required is :{end_time - start_time:.5f} seconds") #gives 5 values after the point (.)

if __name__ == "__main__":
    main()