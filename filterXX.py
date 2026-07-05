checkeven =  lambda no : no % 2 == 0
def main():
    data = [13,12,8,10,11,20]
    print("Input data is ",data)

    Fdata= list(filter(checkeven,data))
    print("Data After Filter :",Fdata)

if __name__== "__main__":
    main()