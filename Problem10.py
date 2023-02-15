## -- Summation of primes -- ##
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math

primes = [2]

def CalculatePrimesNumber(n):
    global primes
        
    #If prime of the index isn't found, looks for it.
    if n > primes[len(primes) - 1]:
        num = primes[-1] + 1 #Starts from the one above last known prime
        
        while True:
            #Try to divide with every primenumber
            isPrime = True
            for k in range(len(primes)):
                #if answer is integer, then number isn't a prime
                if (num % primes[k]) == 0:
                    isPrime = False
                    break
                if primes[k] > math.sqrt(num):
                    break
            if isPrime == True:
                primes.append(num)
            #If enough numbers have been calculated,
            #then will break and return the correct prime
            if n <= num and isPrime == True:
                break
            num += 1
    
    return primes[len(primes) - 1]

#Looks for a prime that is higher than (n)
CalculatePrimesNumber(2000000)
print(sum(primes[:-1]))    
