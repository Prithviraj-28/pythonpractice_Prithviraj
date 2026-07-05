no=11 #global variable

def display():
    a=21    #local variable
    print("from display value of a is ",a)
    print("from display",no)

def demo ():
    print("from demo value of a is ",a) #error
    print("from demo",no)

display()
demo()