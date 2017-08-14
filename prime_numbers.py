def get_prime_numbers(number):
    a = []
    for num in range(2,number):
        status = True
        for i in range(2,num):
            if num % i == 0:
                status = False
        if status:
            a.append(num)
    return a

'''
a = get_prime_numbers(10)
print a
print type(a)
'''
