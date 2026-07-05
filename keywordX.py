def area (radius,PI):
    answer= PI* radius*radius
    return answer 

def main():
    ret=area(PI=3.14,radius=10.5)
    print("Area of circle is :",ret)

if __name__ == "__main__":
    main()
