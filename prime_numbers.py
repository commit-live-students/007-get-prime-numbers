def get_prime_numbers(n):
    import math
    if type(n) != int or n < 1:
        print("Enter an integer greater than 1")
        return 1

    prime_no = []
    for check_prime in range(2,n):
        div = 2
        flag = 0
        while(div <= math.sqrt(check_prime)):
            if(check_prime % div == 0):
                flag = 1
                break
            div += 1
        if flag == 0:
            prime_no.append(check_prime)

    return prime_no
