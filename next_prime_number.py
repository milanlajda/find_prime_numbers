def primenum_check(x):
    counter=0
    for i in range (1, x):
        remainder = x%i
        if remainder == 0:
            counter=counter+1
    if counter > 1:
        pass
    else:
        print "%d is a prime number" %x

def next_prime_num():

    for x in range (1, 1000):
        primenum_check(x)


next_prime_num()
