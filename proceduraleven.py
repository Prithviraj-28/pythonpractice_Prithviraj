def check(No1):
    if No1%2==0:
        print(No1,"is Even Number")
    else:
        print(No1,"is odd Number")

def main():
    value= int(input("Enter the number"))
    check(value)
    

if __name__ == "__main__":
    main()
