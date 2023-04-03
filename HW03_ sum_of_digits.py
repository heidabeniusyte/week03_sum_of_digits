def sum_of_digits(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)

    return sum


if __name__ == "__main__":
    n = 5678


print(sum_of_digits(n))
