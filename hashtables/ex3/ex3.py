def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for arr in arrays:
        for i in arr:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

    for k,v in cache.items():
        if v == len(arrays):
            result.append(k)           


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
