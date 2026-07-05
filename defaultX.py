def area (PI=3.14,radius):            #error because DEFAUT value should be at the last 
    answer= PI* radius*radius
    return answer 

def main():
    ret=area(10.5)
    print("Area of circle is :",ret)

    ret=area(10.5,7.12)
    print("Area of circle is :",ret)


if __name__ == "__main__":
    main()