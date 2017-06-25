def get_prime_numbers(num1):
    not_prime_numbers = [k for i in range(2, 8) for k in range(i*2, num1, i)]
    prime_numbers = [x for x in range(2, num1) if x not in not_prime_numbers]
    return prime_numbers
