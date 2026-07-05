def check(No1):
    if No1%2==0:
        return True
    else:
        return False

def main():
    value= int(input("Enter the number : "))
    ret=check(value)
    if ret == True :
        print("It is even")
    else:
        print("It is odd")
    

if __name__ == "__main__":
    main()