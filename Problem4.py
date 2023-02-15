## -- Largest palindrome product -- #

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def LargestPalindromeProduct():
    PalindromeProducts = []
    num1 = 999
    num2 = 999
    while num1 > 0:
        num2 = 999
        while num2 > 0:
            #print("Num1: " + str(num1) + " Num2: " + str(num2))
            holder = num1 * num2
            holder = str(holder)
            if len(holder) == 6:
                if holder[0] == holder[-1] and holder[1] == holder[-2] and holder[2] == holder[-3]:
                    PalindromeProducts.append(int(holder))
            num2 -= 1
        num1 -= 1
    
    return PalindromeProducts

print(max(LargestPalindromeProduct()))