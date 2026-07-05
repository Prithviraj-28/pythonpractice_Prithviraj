from rajlibrary import filterx,mapx,reducex

checkeven = lambda no : no % 2 == 0
increment = lambda no : no+1
addition= lambda no1,no2 : no1+no2

def main ():
    inputlist= list()
    size=int(input("Enter the size of the string : "))
    for i in range(size):
        value=int(input("Enter Element : "))
        inputlist.append(value)

    Filtereddata=list(filterx(checkeven,inputlist))
    print("The data after filtering is :",Filtereddata)

    incrementeddata=list(mapx(increment,Filtereddata))
    print("The incremented filter data is ",incrementeddata)

    Orignaldata=list(mapx(increment,inputlist))
    print("The incremented orignal data is ",Orignaldata)

    additiondatai = reducex(addition,incrementeddata)
    print("The incremented string addition is ",additiondatai)

    additiondatao = reducex(addition,inputlist)
    print("The addition of orignal string is : ",additiondatao)

        
    
if __name__ == "__main__":
    main()
    