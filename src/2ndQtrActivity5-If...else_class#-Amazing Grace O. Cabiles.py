if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    # if all three sides are equal then it is an equilateral triangle
    if a == b == c:
        print("Equilateral Triangle")
    # if only two sides are equal then it is an isoceles triangle
    elif a == b or b == c or c == a:
        print("Isoceles Triangle")
    # if all three sides are not equal then it is a scalene triangle
    else:
        print("Scalene Triangle")
