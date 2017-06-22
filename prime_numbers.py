# if the number is prime

def is_div(n):
    list_div = 0
    for i in range (2, (n+3)/2):
        if (n%i == 0):
            return False
        else:
            continue
    return True

def get_prime_numbers(p_l):
    prime_list = []
    for i in range(2, p_l+1):
        if (is_div(i) == True):
            prime_list.append(i)

    return prime_list

get_prime_numbers(50)
