#This is a prime number finder.
#White a function that takes an integer and returns a list of all prime numbers up to and including that integer.
def find_primes(n):
    primes=[]
    #for in in range(2,n+1): check if i is a prime number
    for i in range (2,n+1):
        for j in range (2, int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)
    return primes

print (find_primes(16))