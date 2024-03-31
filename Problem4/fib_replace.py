# Function to generate Fibonacci numbers up to a given limit
def fibonacci(limit):
    fib_list = [0, 1]
    a, b = 0, 1
    while b < limit:
        a, b = b, a + b
        fib_list.append(b)
    return fib_list


first_num = 0
second_num = 1
number = int(input("Enter the number to obtain fib series: "))

# Generate Fibonacci numbers up to the given number
fib_numbers = fibonacci(number)

if number == 1:
    print(first_num)
else:
    for i in range(number):
        if i in fib_numbers:
            print(-1)
        else:
            print(i)
