def get_prime_numbers(number1):
    not_prime_numbers = [j for i in range(2, 8) for j in range(i*2, number1, i)]
    prime_numbers = [x for x in range(2, number1) if x not in not_prime_numbers]
    return prime_numbers
