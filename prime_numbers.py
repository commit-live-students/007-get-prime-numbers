def get_prime_numbers(n):
    array = []
    for num in range(0,n):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                array.append(num)
    return array
