import sys

def primeCheck(n):
    if n <= 1:
        raise ValueError('Invalid Input')

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def findPrimes(n):
    if n <= 1:
        raise ValueError('Invalid Input')

    ans = []

    for i in range(2, n+1):
        if primeCheck(i):
            ans.append(i)

    return ans

if __name__ == '__main__':
    n = int(sys.argv[1])
    ans = findPrimes(n)
    ans = list(map(str, ans))
    ans = ' '.join(ans)
    print(ans)
