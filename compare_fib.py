"""
This code compares a list of n Fibonacci and Prime Numbers.

As a new entrant into python programming, I thought this was a
fun project to do.
It contains three methods:

get_fib(n): genearates a list of n fibonacci numbers and stores them in
fib.

is_prime(n) -> bool: Returns True if n is prime, false otherwise. it is a helper
function to gen_prime.

gen_prime(size) ->list: returns a list of length `size` with `size` primes
"""

fib = []

#Generate fibonacci list
def get_fib(n):
    fib.append(0)
    fib.append(1)
    for x in range(2, n):
        fib.append(fib[x - 1] + fib[x - 2])

#Generate primes
def is_prime(n):
	if n > 1:
		if n == 2:
			return True
		if n % 2:
			for x in range(3, n//2):
				if not n % x:
					return False
			return True
		return False
	return False


def gen_primes(size):
	primes = []
	count = 0
	while len(primes) < size:
		if is_prime(count):
			primes.append(count)
		count += 1
	return primes

#Generate Fibonacci and primes
get_fib(30)
all_primes = gen_primes(1000)

#Making the comparison
size = min(len(fib), len(all_primes))

for grt in range(size):
    if fib[grt] in all_primes:
        print(fib[grt], end = ' ')
