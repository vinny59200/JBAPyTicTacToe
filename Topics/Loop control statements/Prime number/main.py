number = int(input())


def is_prime_number(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if is_prime_number(number):
    print("This number is prime")
else:
    print("This number is not prime")
