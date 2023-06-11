import sys

def process(n):
    n = str(n)
    n = list(map(int, n))
    return n

def isIncreasing(n):
    n = process(n)
    for i in range(len(n)-1):
        if n[i] >= n[i+1]:
            return False

    return True

def countIncreasing(n):
    ans = 0

    for i in range(1, n+1):
        if isIncreasing(i):
            ans += 1

    return ans

if __name__ == '__main__':
    n = sys.argv[1]
    n = int(n)
    print(countIncreasing(n))
