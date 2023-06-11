from stats import process

def findTriplets(arr):
    if len(arr) < 3:
        return []
    sorted_arr = sorted(arr)
    ans = set()

    for key, value in enumerate(arr[:-2]):
        if key >= 1 and value == arr[key - 1]:
            continue

        temp_dict = dict()
        for val in arr[key+1:]:
            if val not in temp_dict:
                temp_dict[-value-val] = 1
            else:
                ans.add((value, -value-val, val))

    return list(ans)

if __name__ == '__main__':
    arr = []

    while True:
        a = input()
        if a == '-12345':
            break
        else:
            arr.append(a)

    arr = process(arr)
    triplets = findTriplets(arr)
    triplets = [map(str, triplet) for triplet in triplets]
    if len(triplets) > 1:
        print(str(len(triplets)) + " triples found:")
    elif len(triplets) == 1:
        print("1 triple found:")
    else:
        print("0 triples found")
    for triple in triplets:
        print(', '.join(triple))
