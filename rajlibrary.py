

def filterx(Task,elements):
    Result=list()

    for i in elements:
        ret  = Task(i)
        if ret == True :
            Result.append(i)
    
    return Result

def mapx(Task,Elements):
    Result=list()
    
    for i in Elements:
        ret = Task(i)
        Result.append(ret)

    return Result


def reducex(Task,Elements):
    sum=0
    for i in Elements:
        sum = Task(sum,i)

    return sum
