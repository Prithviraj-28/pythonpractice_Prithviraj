def summation(data):
    sum=0

    for no in data:
        sum=sum + no
    
    return sum

def main():
    size=0
    arr = list()
    size=int(input("Enter the number of elements:"))
    
    print("enter the elements")
    for i in range(size):
        no=int(input())
        arr.append(no)

    ret=summation(arr)
    print("summation is ",ret)

    
if __name__ == "__main__":
    main()