checkeven = lambda no : no%2==0

incriment =  lambda no : no +1

addition= lambda no1,no2: no1+no2 

def filterx(Task,Elements):
    result= list()
    for no in Elements:
        ret=Task(no)    #checkeven(no)
        if ret == True:
            result.append(no)

    return result

def mapx(task,elements):
    result=list()
    for no in elements:
        ret=task(no)     #increment no
        result.append(ret)

    return result

def reduceX(Task,elements):
    sum=0
    for no in elements:
        sum=Task(sum,no)

    return sum



def main():
    data = [13,12,8,10,11,20]
    print("Input data is ",data)

    Fdata= list(filterx(checkeven,data))
    print("Data After Filter :",Fdata)

    Mdata=list(mapx(incriment,Fdata))
    print("Data After Map :",Mdata)

    Rdata= reduceX(addition,Mdata)
    print("Data after reduce :",Rdata)

if __name__== "__main__":
    main()