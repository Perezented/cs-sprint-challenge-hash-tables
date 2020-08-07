

combined_weights = {}
weights_legend = {}


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    if length == 1:
        return None
    result = []
    if length == 2:
        if weights[0] + weights[1] == limit:
            return (1, 0)
        else:
            return None
    print()
    print()
    print('weights:')
    print(weights)
    print('limit:')
    print(limit)
    print()
    print()

    # Your code here
    # weights.sort(reverse=True)
    i = 0
    while i != length:
        # print(weights[i])
        weights_legend[weights[i]] = i
        # weights.sort(reverse=True)
        combined_weights[weights[i]] = limit - weights[i]
        i += 1
    for j in range(length - 1):
        print()
        # print(f'index: {j}')
        # print(f'weights: {weights[j]}')
        # print(f'combined_weights value: {combined_weights[weights[j]]}')
        if combined_weights[weights[j]] in combined_weights:
            print('its here')
            print(combined_weights[weights[j]])
            print(weights[j])
            result = (weights_legend[weights[j]],
                      weights_legend[combined_weights[weights[j]]])
    # for k, v in combined_weights.items():
    #     print(k, v)
    #     print(combined_weights[k])
    #     print(v)
    #     print(f'math here: {limit - k}')
    #     if
    # print(len(combined_weights))
    # u = length - 1
    # while u != -1:
    #     if limit < weights[u]:
    #         None
    #     else:
    #         print(weights[u])
    #         print(u)

    #     u -= 1

    # u = length - 1

    # while u != -1:
    #     print(weights[u])
    #     u -= 1
    #     for w in weights:
    #         if weights[u] + w == limit and w != weights[u]:
    #             result.append(w)
    print()
    print()
    print('combined_weights:')
    print(combined_weights)
    print(weights_legend)
    print()
    print('Results:')
    print(result)
    print()
    return result
    # t = length - 1

    # while t != -1:
    #     print(weights[t])
    #     if weights[t] == limit:
    #         return (0, t)
    #     t -= 1
