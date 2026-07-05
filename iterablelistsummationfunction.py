def summation(data):
    sum=0
    for no in data:
        sum=sum+no
    return sum


def main():
    marks=[78,90,56,98,77]
    ret=summation(marks)

    print ("Addition is ",ret)
    

if __name__ == "__main__":
    main()