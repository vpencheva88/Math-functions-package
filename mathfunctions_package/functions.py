#function to find the greatest common divisor
def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('gcd only works with integers.')
    a,  b = abs(a), abs(b)  #absolute values (only positive values) of a and b
    while b:
        a, b = b, a % b
    return a

#function to find the lowest common multiple
def lcm(a: int, b:int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('lcm only works with integers.')
    if a == 0 or b == 0:
        return 0 #without this system would crash, as it would do lcm(0,0)/gcd(0,0)
    return abs(a * b) // gcd(a, b)

#function to find primes numbers from a set of numbers
def primes(n: int) -> list[int]:
    """A list of all prime numbers between 2 and n:"""
    primes = []
    for number in range(2, n + 1):
        divisors = 0
        for d in range(2, int(number ** 0.5) + 1):
            if number % d == 0: #checks for no remainders
                divisors += 1 
        if divisors == 0: #nothing divided it, so it is prime
            primes.append(number) #adds this number, which we have found to be prime to the list
    return primes



