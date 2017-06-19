
def get_prime_numbers(num=1):
    prime = []
    flag = 0
    for i in range(2,num+1):
        flag = 0
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
    return prime

print get_prime_numbers(30)
