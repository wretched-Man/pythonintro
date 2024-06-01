#this program does not properly satisfy the requirements. It can generate
#a list of numbers divisible by 7 and in reverse, but is, however,
#very slow.
#https://www.reddit.com/r/dailyprogrammer/comments/3irzsi/20150828_challenge_229_hard_divisible_by_7/

def div_seven(n:int = 1000):
    """
    Find the sum of all positive integers between 0 and 10^11 that are
    divisible by 7, and are also divisible by 7 when you reverse the digits.
    e.g. 259 and 952
    """

    divisibles = set()

    for x in range(0,n,7):
        rev_x = int(str(x)[::-1])

        if not rev_x % 7:
            divisibles.add(x)
            divisibles.add(rev_x)


    return sorted(divisibles)[1:]
print(div_seven(10**5))