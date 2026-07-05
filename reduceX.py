from functools import reduce 
checkeven = lambda no : no%2==0

incriment =  lambda no : no +1

def addition(no1,no2):
    return no1+no2 

def main():
    data = [13,12,8,10,11,20]
    print("Input data is ",data)

    Fdata= list(filter(checkeven,data))
    print("Data After Filter :",Fdata)

    Mdata=list(map(incriment,Fdata))
    print("Data After Map :",Mdata)

    Rdata= reduce(addition,Mdata)
    print("Data after reduce :",Rdata)

if __name__== "__main__":
    main()