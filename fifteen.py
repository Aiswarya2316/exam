def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

a=int(input("enter a number:"))
print(f"Factorial of {a} is:", factorial(a))
