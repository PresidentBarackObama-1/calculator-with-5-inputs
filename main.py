def add(v, w, x, y, z):
    return v + w + x + y + z


def subtract(v, w, x, y, z):
    return v - w - x - y - z


def multiply(v, w, x, y, z):
    return v * w * x * y * z


def divide(v, w, x, y, z):
    return v / w / x / y / z


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        num5 = float(input("Enter fifth number: "))

        if choice == '1':
            print(num1, "+", num2, "+", num3, "+", num4, "+", num5, '=', add(num1, num2, num3, num4, num5))

        elif choice == '2':
            print(num1, "-", num2, "-", num3, "-", num4, "+", num5, "=", subtract(num1, num2, num3, num4, num5))

        elif choice == '3':
            print(num1, "*", num2, "*", num3, "*", num4, "*", num5, "=", multiply(num1, num2, num3, num4, num5))

        elif choice == '4':
            print(num1, "/", num2, "/", num3, "/", num4, "/", num5, "=", divide(num1, num2, num3, num4, num5))

        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break

    else:
        print("Invalid Input")
