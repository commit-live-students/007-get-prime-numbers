def get_prime_numbers(newNum):
    num_list = []
    flag = 0
    if(newNum > 1):
        for i in range (2,newNum+1):
            flag = 0
            for j in range (2,i):
                if(i%j == 0):
                    flag = 1
                    break
            if flag == 0:
                num_list.append(i)
                print num_list
        return num_list
    else:
        print "Enter number greater than 1"

print get_prime_numbers(10)
