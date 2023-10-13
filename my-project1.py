def add_numbers(*args):
    return sum(args)

num_count = int(input("Enter the number of values you want to add: "))
numbers = []

for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

result = add_numbers(*numbers)
print("The sum of the numbers is:", result)

