for i in range(10, 25):
    for j in range(2, i):
        if i % j == 0:
            print("%d is not primes" %i)
            break
    else:
        print("%d is primes" %i)