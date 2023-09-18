def fn(n):
    if n <= 0:
        return "Error in input"
    elif n <= 2:
        return n - 1
    else:
        return fn(n - 1) + fn(n - 2)

num = int(input("Enter a number: "))
result = fn(num)
print(f"fn({num}) = {result}")
