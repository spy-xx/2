def base_conversion(value, base_from, base_to):
    decimal_value = 0
    for i, digit in enumerate(value[::-1]):
        decimal_value += int(digit) * (base_from ** i)

    result = []
    while decimal_value > 0:
        remainder = decimal_value % base_to
        if remainder < 10:
            result.append(str(remainder))
        else:
            result.append(chr(ord('A') + (remainder - 10)))
        decimal_value //= base_to

    return ''.join(result[::-1])

num1 = input("Enter a binary number: ")
print(base_conversion(num1, 2, 10))

num2 = input("Enter an octal number: ")
print(base_conversion(num2, 8, 16))
