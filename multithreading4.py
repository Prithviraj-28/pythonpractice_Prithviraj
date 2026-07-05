import threading

def display(no1,no2,no3):
    print(f"Inside Display {no1},{no2},{no3} ",threading.get_ident())
    
def main():
    print(f"Inside main ",threading.get_ident())

    tobj= threading.Thread(target=display, args=(11,21,51,))  #(11,21,51,) converts the int to tuple

    tobj.start()

if __name__ == "__main__":
    main()