import threading

def display(no):
    print(f"Inside Display {no} ",threading.get_ident())
    
def main():
    print(f"Inside main ",threading.get_ident())

    tobj= threading.Thread(target=display, args=(11,))  #(11,) converts the int 11 to tuple

    tobj.start()

if __name__ == "__main__":
    main()