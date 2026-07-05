#Factorial code
#6 = 1 * 2 * 3 * 4 * 5 * 6
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    
    return fact

def main ():
    value = int(input("Enter the number : "))
    ret = factorial(value)
    print(f"Factorial of {value} is : ",ret)   #formatted printing

if __name__ == "__main__":
    main()