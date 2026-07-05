check= lambda No1: No1%2==0

def main():
    value= int(input("Enter the number : "))
    ret=check(value)     #ret=value % 2 == 0
    if ret == True :
        print("It is even")
    else:
        print("It is odd")
    

if __name__ == "__main__":
    main()