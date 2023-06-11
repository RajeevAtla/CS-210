import primes
import sys

def getFactors(n):
    if n <= 1:
        return n
    if primes.primeCheck(n):
        return n

    possibleFactors = primes.findPrimes(n)
    ans = []

    for factor in possibleFactors:
        while n % factor == 0:
            ans.append(factor)
            n /= factor

    return ans

if __name__ == '__main__':
    n = int(sys.argv[1])
    ans = getFactors(n)
    if type(ans) == list:
        ans = list(map(str, ans))
        ans = ' '.join(ans)
    print(ans)
