def next_prime_num():
    print "Current prime number is 1. Continue? Y N"
    x=2
    for y in range (2, 100):
        x=y
        if (x)%(x-1) != 0:
            print "Next prime number is %s" %x
        else:
            continue


        x=x+1

next_prime_num()




