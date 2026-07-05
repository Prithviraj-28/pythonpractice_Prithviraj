from marvellous import Addition, Substraction

def main():
    print("Enter First number :")
    value1= int(input())

    print("Enter second number :")
    value2= int(input())

    ret1= Addition(value1 , value2)
    ret=Substraction(value1,value2)
    print("Addition is ",ret1)
    print("Substraction is ",ret) #error


if __name__ == "__main__":
    main()