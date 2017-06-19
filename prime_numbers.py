def get_prime_numbers(n):
    prime_numbers = []
    for num1 in range(2,n+1):
        for num2 in range(2, num1):
            if (num1 % num2 == 0):
                break;
        else:
            prime_numbers.append(num1)
    return prime_numbers

n = 20
get_prime_numbers(n)
