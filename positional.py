def area (radius,PI):
    answer= PI* radius*radius
    return answer 

def main():
    ret=area(10.5,3.14)
    print("Area of circle is :",ret)

    ret=area(13.6,7.12)
    print("Area of circle is :",ret)


if __name__ == "__main__":
    main()
