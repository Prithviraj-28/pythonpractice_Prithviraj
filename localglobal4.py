no=11 #global variable

def display():
    global no
    no = 21
    print("from display",no)

print("Before",no)
display()
print("After",no)   