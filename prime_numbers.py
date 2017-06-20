def get_prime_numbers(num_range):
    List = []
    for num in range(num_range + 1):
       # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                List.append(num)
    return List

get_prime_numbers(20)
