def perform_operations(a, b, c, d, e, f, g):
    addition_result = a + b + c + d + e + f + g
    multiplication_result = a * b * c * d * e * f * g
    subtraction_result = a - b - c - d - e - f - g
    return addition_result, multiplication_result, subtraction_result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))
num6 = float(input("Enter the sixth number: "))
num7 = float(input("Enter the seventh number: "))

addition, multiplication, subtraction = perform_operations(num1, num2, num3, num4, num5, num6, num7)

print("The sum of {}, {}, {}, {}, {}, {}, and {} is: {}".format(num1, num2, num3, num4, num5, num6, num7, addition))
print("The multiplication of {}, {}, {}, {}, {}, {}, and {} is: {}".format(num1, num2, num3, num4, num5, num6, num7, multiplication))
print("The subtraction of {}, {}, {}, {}, {}, {}, and {} is: {}".format(num1, num2, num3, num4, num5, num6, num7, subtraction))
