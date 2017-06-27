def get_prime_numbers(inputNumb):
    numb_list = []
    a = 0
    if(inputNumb > 1):
        for i in range (2,inputNumb+1):
            a = 0
            for j in range (2,i):
                if(i%j == 0):
                    a = 1
                    break
            if a == 0:
                numb_list.append(i)
        return numb_list
    else:
        print "Enter number greater than 1"

get_prime_numbers(10)
