#Largest prime factor

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
num = 600851475143
PrimeFactors = []
Primes = [2]

def FindNextPrime():
    global Primes
    holder = Primes[-1]
    while True:
        holder += 1
        for i in range(len(Primes)):
            if (holder / Primes[i]).is_integer() == False:
                Primes.append(holder)
                return

#Process will be repeeated till number is reduced to one.
while num > 1:
    #Tries to divide with every prime number
    for i in range(len(Primes)):
        if (num / Primes[i]).is_integer() == True: #If result is an integer.
            PrimeFactors.append(Primes[i])
            num = num / Primes[i]
            break
    FindNextPrime()
print("PrimeFactors: " + str(PrimeFactors[-1]))