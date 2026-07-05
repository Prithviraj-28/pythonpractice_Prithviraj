def check(No1):
    return No1%2==0

def main():
    value= int(input("Enter the number : "))
    ret=check(value)
    if ret == True :
        print("It is even")
    else:
        print("It is odd")
    

if __name__ == "__main__":
    main()