#Given a digit n, make it into a palindrome
#List out the no. of steps taken to achieve this
#https://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/
 
def make_palindrome(n:int):
    """
    Convert any given number n into a palindrome.

    This is done by reversing the digits and appending and then repeating the steps
    until you get a palindromic number. Some require many steps. e.g.
    
    24 gets palindromic after 1 steps: 66 -> 24 + 42 = 66
    
    28 gets palindromic after 2 steps: 121 -> 28 + 82 = 110, so 110 + 11 (110 reversed) = 121.

    The task is to list out the number of steps taken to make n palindromic.
    """
    result = [n]
    steps = 0
    while((n != int(str(n)[::-1])) and steps < 10000):
        steps += 1
        n += int(str(n)[::-1])
    
    result.append([steps, n])
    return result
print(make_palindrome(196196871))
