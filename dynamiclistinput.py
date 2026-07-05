
def main():
    size=0
    arr = list()
    size=int(input("Enter the number of elements:"))
    
    print("enter the elements")
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)



if __name__ == "__main__":
    main()