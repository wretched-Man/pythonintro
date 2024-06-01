#Given a string with specific constraints, verify if it is an ISBN number.
#https://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/
def is_isbn(n:str):
    """
    Check if a string reps an ISBN number
    """
    result = 0
    for pos,elem in enumerate(n):
        if elem == 'X':
            result += (10 * (10 - pos))
            continue
        result += (int(elem) * (10 - pos))

    if not result % 11:
        return True
    return False
        


#Generate a random ISBN Number
#0-7475-3269-9 format
from random import randint

def gen_isbn():
    """
    Generate and return a random ISBN number
    of like format as 0-7475-3269-9
    """
    while True:
        test_isbn = str(randint(0, 9)) + str(randint(0, 9999)).zfill(4) + \
        str(randint(0, 9999)).zfill(4)

        digit = randint(0, 10)

        if digit == 10:
            test_isbn += 'X'
        else:
            test_isbn += str(digit)

        assert len(test_isbn) == 10

        if is_isbn(test_isbn) == True:
            return test_isbn

#test code
#Generate 1000 ISBN numbers
isbn_set = set()
while len(isbn_set) != 1000:
    isbn_set.add(gen_isbn())

print(isbn_set)
