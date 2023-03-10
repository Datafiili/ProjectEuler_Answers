#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

Fibonacci = [1,2]
number = 0
while number < 4000000:
    number = Fibonacci[len(Fibonacci) - 2] + Fibonacci[len(Fibonacci) - 1]
    if number < 4000000:
        Fibonacci.append(number)

total = 0
for i in range(len(Fibonacci)):
    if Fibonacci[i] % 2 == 0:
        total += Fibonacci[i]

print(total)