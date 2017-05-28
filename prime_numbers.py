def get_prime_numbers(inputNum):
    num_list = []
    flag = 0
    if(inputNum > 1):
        for i in range (2,inputNum+1):
            flag = 0
            for j in range (2,i):
                if(i%j == 0):
                    flag = 1
                    break
            if flag == 0:
                num_list.append(i)
        return num_list
    else:
        print "Enter number greater than 1"

get_prime_numbers(10)
