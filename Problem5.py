## -- Smallest multiple -- ##

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## -------------------- Least Common Multiple -------------------- ##
#Written by: Aarni Junkkala

import GreatestCommonDivisor as GCD #Required
def LCM(numbers):
    ## ----- Return and Fail conditions ----- ##

    #Must be a list
    if type(numbers) != list:
        return False
    
    #Null list or list of one value returns false
    if len(numbers) == 0 or len(numbers) == 1:
        return False
    
    #If any of the numbers isn't a integer, then return False
    for i in range(len(numbers)):
        if isinstance(numbers[i], float) or isinstance(numbers[i],int):
            if float(numbers[i]).is_integer() == False:
                return False
        else:
            return False

    #If any of numbers is zero, return false
    for i in range(len(numbers)):
        if numbers[i] == 0:
            return False

    ## ----- Converts all numbers to positive numbers ----- ##
    for i in range(len(numbers)):
        numbers[i] = abs(numbers[i])
    
    ## ----- Processing itself ----- ##
    #If list is longer than two, code repeats to formula to each number and the result
    num = numbers[0]
    for i in range(1, len(numbers)):
        result = (num * numbers[i]) / (GCD.GCD([num,numbers[i]])) #Formula
        num = result
    return result

print(LCM([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))