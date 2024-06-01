#Abundant and deficient Numbers
#https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

def is_abundant(n:int):
    """
    Given a number, n, output whether it is abundant or deficient.

    In number theory, a deficient number is a number n for which the sum of divisors
    sigma(n)<2n, or, equivalently, the sum of proper divisors (or aliquot sum) s(n)<n. The value
    2n - sigma(n) (or n - s(n)) is called the number's deficiency. In contrast, an abundant number
    or excessive number is a number for which the sum of its proper divisors is greater than the
    number itself. As an example,
    
    consider the number 21. Its divisors are 1, 3, 7 and 21, and their sum is 32. Because 32 is less
    than 2 x 21, the number 21 is deficient. Its deficiency is 2 x 21 - 32 = 10.

    The integer 12 is the first abundant number. Its divisors are 1, 2, 3, 4, 6, and 12, and their
    sum is 28. Because 28 is greater than 2 x 12, the number 12 is abundant.
    It's abundant by 4 28 - 24 = 4.

    @param n: number to check for deficiency/abundance
    """

    #Count divisors
    sum_of_divisors = []
    for x in range(1, n//2 + 1):
        if (x in sum_of_divisors) or (n//x in sum_of_divisors):
            continue
        elif n % x == 0:
            sum_of_divisors.append(x)
            sum_of_divisors.append(n//x)

    divisors = sum(sum_of_divisors)
    if divisors > (n * 2):
        return f'{n} abundant by {(divisors - (n * 2))}.'
    elif divisors < (n * 2):
        return f'{n} deficient.'
    else:
        return f'{n} is perfect.'

#Check 1000 for abundance
print(is_abundant(1000))