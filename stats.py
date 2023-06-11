import math


def mean(arr):
    return sum(arr)/len(arr)

def std(arr):
    m = mean(arr)
    return math.sqrt((1/(len(arr) - 1)) * sum([(value - m)**2 for value in arr]))

def median(arr):
    n = len(arr)

    sorted_arr = sorted(arr)
    if n % 2 != 0:
        return sorted_arr[n//2]
    else:
        return (sorted_arr[n//2] + sorted_arr[n//2 - 1])/2

def process(arr):
    return list(map(int, arr))

if __name__ == '__main__':
    arr = []

    while True:
        a = input()
        if a == '-12345':
            break
        else:
            arr.append(a)

    arr = process(arr)

    print('mean: ' + str(mean(arr)))
    print('median: ' + str(median(arr)))
    print('standard deviation: ' + str(std(arr)))
