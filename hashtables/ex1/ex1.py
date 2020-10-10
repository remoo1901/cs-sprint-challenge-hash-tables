def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here


    cache = {}

    for i in range(length):
        cur_value = weights[i]

        if cur_value in cache:
          return (i, cache[cur_value])

        weight_diff = limit - cur_value

        cache[weight_diff] = i

    return None

weights = [4, 6, 10, 15, 16]
length = 5
limit = 21
print(get_indices_of_item_weights(weights, length, limit))
